import asyncio
from temporalio.worker import Worker
from temporalio.client import Client
from workflows import MoneyWithDrawalWorkflow
from activities import check_account_balance, validate_money_withdrawal


async def main():
    # use the below code if you want to run this orchestration with docker
    # client = await Client.connect('temporal:7233', namespace='default')
    # use the below code if you want to run this orchestration without docker
    client = await Client.connect('localhost:7233', namespace='default')
    worker = Worker(
        client=client, workflows=[MoneyWithDrawalWorkflow],
        activities=[check_account_balance, validate_money_withdrawal],
        task_queue='money-withdraw-task-queue'
    )
    await worker.run()


def run_worker():
    asyncio.run(main())
