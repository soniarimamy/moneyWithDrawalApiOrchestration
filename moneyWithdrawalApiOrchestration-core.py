import uvicorn
from helpers.constants import global_variables


# create config object
withdraw_money_api_orchestration_config = uvicorn.Config(
    app='money-withdrawal-api-orchestration:app', host=global_variables['MONEY_WITHDRAWAL_ORCHESTRATION_API_HOST'],
    port=int(global_variables['MONEY_WITHDRAWAL_ORCHESTRATION_API_PORT']), reload=False, log_level="info"
)

opencrvs_openapi_server = uvicorn.Server(withdraw_money_api_orchestration_config)
opencrvs_openapi_server.run()
