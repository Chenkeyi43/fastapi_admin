from fastapi import FastAPI
from admin.controller.login import login_router
from admin.controller.role import role_router
from admin.controller.user import user_router
import uvicorn


app = FastAPI()

router_list = [
    {'router': login_router, 'tags': ['登录路由']},
    {'router': user_router, 'tags': ['用户路由']},
    {'router': role_router, 'tags': ['角色路由']},

]

for router in router_list:
    # 使用 app.include_router()，我们可以将每个 APIRouter 添加到主 FastAPI 应用程序中
    app.include_router(router=router.get('router'),tags=router.get('tags'))

if __name__ == '__main__':
    uvicorn.run(
        app='app:app',
        host='127.0.0.1',
        port=8080,

    )
