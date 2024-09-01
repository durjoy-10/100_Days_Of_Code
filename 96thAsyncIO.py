import asyncio
import requests
 
async def function1():
    print("Fun 1")
    URL="ANd9GcSflDToHEogmeUrcqnzIxd1r1d2X9sGX5YaunfxCkCJLw"
    responce= requests.get(URL)
    open("Image1.jpg","wb").write(responce.content)
    return "Durjoy"
    
async def function2():
    print("Fun 2")
    URL="ANd9GcSUyA00kouwUQT5GEDViZAy26i231zkpQBRExGSBKUT4w"
    responce= requests.get(URL)
    open("Image2.jpg","wb").write(responce.content)
    return "Das"

async def function3():
    print("Fun 3")
    URL="ANd9GcSecufdWJLGgae4j1KG_1RlNsvo3YlpMgMYNf_4s5Q1xw"
    responce= requests.get(URL)
    open("Image2.jpg","wb").write(responce.content)
    return "2102017"
async def main():
    await function1()
    await function2()
    await function3()
    
    L=await asyncio.gather(
        function1(),
        function2(),
        function3()
    )
    print(L)