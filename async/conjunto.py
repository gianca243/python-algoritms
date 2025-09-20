import asyncio, multiprocessing, time, random
from enum import Enum

class Status(Enum):
    START = 'START 🔘'
    PENDING = 'PENDING 🚧'
    CANCELED = 'CANCELED ❌'
    FINISHED = 'FINISHED 🎉'

def logger(order_id: int, status: Status, message: str):
     print(f'[order_id: {order_id}], status: {status.value}, message: {message}')

async def check_inventory(order_id, item):
    logger(order_id, Status.START, f'Verificado Inventario para item {item}')
    await asyncio.sleep(random.randint(3,6))
    
    logger(order_id, Status.START, f'Inventario verificado para {item}')
    print("------------------------------------------------------------------------------------")
    #simulando disponibilidad
    return [item, random.choice([True, False])]

async def process_payment(order_id):
    logger(order_id, Status.PENDING, 'Enviando a procesar pago')
    await asyncio.sleep(random.randint(2,3))
    logger(order_id, Status.FINISHED, 'Pago procesado correctamente')
    print("------------------------------------------------------------------------------------")
    return True

#Funcion intensiva en CPU para calcular el costo total del pedido
def calculate_total(order_id, items):
    logger(order_id, Status.START, f'Calculado el costo total para {len(items)} articulos..')
    time.sleep(5)
    total = sum(item['price'] for item in items)
    logger(order_id, Status.START, f'Costo total de la orden es: {total}')
    print("------------------------------------------------------------------------------------")
    return total

async def process_order(order_id, items):
    print(f'[order_id: {order_id}], status: START, message: iniciando proceso')
    logger(order_id, Status.START, 'Iniciando proceso')
    inventory_checks = [check_inventory(order_id, item['name']) for item in items]
    inventory_result = await asyncio.gather(*inventory_checks)
    result = [item for item in inventory_result if item[1] == False]
    if result:
        logger(order_id, Status.CANCELED, f'Productos {result[0][0]} no disponibles')
        return
        
    with multiprocessing.Pool() as pool:
        total = pool.apply(calculate_total, (order_id, items,))

    #procesar pago 
    payment_result = await process_payment(order_id)
    
    if payment_result:
        logger(order_id, Status.FINISHED, f'Procesado correctamente total {total}')
    else:
        logger(order_id, Status.CANCELED, f'El pago no puedo ser completado')
    print("------------------------------------------------------------------------------------")
        
async def main():
    orders = [
        {'order_id': 1, 'items': [{'name': 'Laptop', 'price': 1000}, {'name': 'Mouse', 'price': 50}]},
        {'order_id': 2, 'items': [{'name': 'Teclado', 'price': 80}, {'name': 'Monitor', 'price': 300}]},
        {'order_id': 3, 'items': [{'name': 'Smartphone', 'price': 700}, {'name': 'Funda', 'price': 20}]}
    ]

    #Procesar múltiples órdenes concurrentemente
    tasks = [process_order(order['order_id'], order['items']) for order in orders]
    await asyncio.gather(*tasks)
    
## creación de event loop

if __name__ == '__main__':
    asyncio.run(main())