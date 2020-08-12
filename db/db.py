import aiomysql
from main_func import event_loop


async def create_db():
    with open("create_db.sql", "r") as create_db_command:
        conn = await aiomysql.connect(host='127.0.0.1', port=3306,
                                      user='root', password='new_password', db='mysql',
                                      loop=event_loop)
        cur = await conn.cursor()
        await cur.execute(create_db_command)
        await cur.close()
        conn.close()


async def create_pool():
   return await aiomysql.create_pool(host='127.0.0.1', port=3306,
                                      user='root', password='new_password', db='mysql',
                                      loop=event_loop)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(create_db())
