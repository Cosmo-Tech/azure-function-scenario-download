# CosmoTech/azure-function-scenario-download

This function display a usage of the Accelerator created to generate Azure Functions in a Cosmotech API scenario context

## Required configuration

### Application settings
In your Function app settings you will need the following keys to be set up :

The settings to link to the Cosmotech API:

- `COSMOTECH_API_HOST` : The host address used to access your api instance
- `COSMOTECH_API_SCOPE` : The scope of your api instance

From an azure app registration having read authorization for the Cosmotech API:

- `AZURE_TENANT_ID`
- `AZURE_CLIENT_ID`
- `AZURE_SECRET_ID` 

## Sample endpoints

### ScenarioDownload

This simple endpoint is the minimal code required to create an Azure Function, its outputs are documented in the [following page](function_output.md)

### CountADT

This endpoint load an ADT source and return the number of twins and relations per type 