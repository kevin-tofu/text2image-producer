import os
import io
import asyncio
from PIL import Image
from fastapi import APIRouter, Depends
from fastapi import File, UploadFile
from fastapi import BackgroundTasks, Response
from fastapi import WebSocket
# from fastapi.responses import HTMLResponse
from celery.result import AsyncResult
import dataclasses  # import dataclass, asdict


from src import routes_depends
from src.config import config_org as config
from src.publisher import app
from src import tools
router = APIRouter(prefix="")
# 
# https://github.com/derlin/fastapi-notebook-runner/blob/main/nb_runner/main.py
# 


# @router.get('/')
# def getTasks():
#     tasks = app.control.inspect()
#     return tasks.active()


# @router.delete('/')
# def getTasks():
#     tasks = app.control.inspect()
#     return tasks.active()


@router.post(
    '/prompt',
    description="",
)
def post_prompt(
    # params: dict = Depends(routes_depends.params_diffuser)
    params: routes_depends.params_diffuser=Depends(routes_depends.params_diffuser)
):
    """
    """
    
    params_dict = dataclasses.asdict(params)
    # print(type(params))
    # print('params:', params_dict)
    task = app.send_task(
        'main.prompt', 
        args=[],
        kwargs=params_dict
    )
    return dict(task_id=task.task_id)



@router.get(
    '/prompt/{task_id}',
    description="",
)
def get_prompt(
    task_id: str
):
    """
    """
    
    task = AsyncResult(task_id)
    return task.info


@router.delete(
    '/prompt/{task_id}',
    description="",
)
def delete_prompt(
    task_id: str
):
    """
    """
    
    task = AsyncResult(task_id)
    # task.info
    task.revoke(terminate=True)


    return 'revoked'


@router.get(
    '/image/{task_id}',
    description="",
)
def get_image(
    task_id: str
):
    """
    """

    extention = 'png'
    image_path: str = f"{config.data_path}/{task_id}.{extention}"
    if os.path.exist(image_path):

        image = Image.open(image_path)

        with io.BytesIO() as buffer:

            image.save(buffer, format=extention)
            image_bytes = buffer.getvalue()
        
            return Response(content=image_bytes, media_type=f"image/{extention}")


    else:
        return dict(
            status='failed'
        )


@router.post(
    '/image/{task_id}',
    description="",
)
async def post_image(
    task_id: str,
    image: UploadFile = File(...),
    bgtask: BackgroundTasks = BackgroundTasks(),
):
    """
    """
    
    extention = tools.get_file_extension(image.filename)
    # ftype_input = tools.check_filetype(fname_org)

    image_path: str = f"{config.data_path}/{task_id}.{extention}"
    image = Image.open(io.BytesIO(await image.read()))
    image.save(image_path)
    # return handler.post_file_BytesIO("transferred-image", file, bgtask, **params)

    bgtask.add_task(tools.remove_file, image_path)


@router.websocket("/image/{task_id}/status")
async def websocket_endpoint(websocket: WebSocket, task_id: str):

    await websocket.accept()

    while True:
        task = AsyncResult(task_id)
        if task.state == 'PENDING':
            # await websocket.send_text("Task is pending")
            await websocket.send_json(dict(status='pending'))

        elif task.state == 'STARTED':
            await websocket.send_json(dict(status='started'))

        elif task.state == 'PROGRESS':
            await websocket.send_json(task.info | dict(status='progress'))

        elif task.state == 'SUCCESS':
            await websocket.send_json(task.info | dict(status='success', result=task.result))
            break
        else:
            await websocket.send_json(task.info | dict(status='failure', result=task.result))
            break
        
        await asyncio.sleep(5)
