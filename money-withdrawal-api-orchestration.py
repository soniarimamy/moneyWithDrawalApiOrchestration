import uuid
import threading
from fastapi import FastAPI
from run_worker import run_worker
from temporalio.client import Client
from contextlib import asynccontextmanager
from workflows import MoneyWithDrawalWorkflow
from schemas.common_schemas import CustomHttpRequestError
from schemas.account_schemas import IMoneyWithDrawalValidation


@asynccontextmanager
async def lifespan(_a: FastAPI):
    thread = threading.Thread(target=run_worker, daemon=True)
    thread.start()
    yield


app = FastAPI(
    title='Rest API for web services orchestration on a bank',
    docs_url='/bank/docs',
    redoc_url='/bank/redoc',
    openapi_url='/bank/openapi.json',
    version='1.0.0',
    lifespan=lifespan
    )


@app.post('/with-draw')
async def with_draw_money(money_with_draw_validation: IMoneyWithDrawalValidation | CustomHttpRequestError):
    workflow_id = f'money-withdraw-workflow-{uuid.uuid1()}'
    # use the below code if you want to run this orchestration with docker
    # client = await Client.connect('temporal:7233')
    # use the below code if you want to run this orchestration without docker
    client = await Client.connect('localhost:7233')

    result = await client.execute_workflow(
        MoneyWithDrawalWorkflow.run, money_with_draw_validation,
        id=workflow_id, task_queue='money-withdraw-task-queue'
    )
    return {'result': result}
