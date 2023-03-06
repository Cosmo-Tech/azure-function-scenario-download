# azure-function-scenario-download

[![Documentation Status](https://readthedocs.org/projects/cosmotech-azure-function-scenario-download/badge/?version=latest)](https://cosmotech-azure-function-scenario-download.readthedocs.io/en/latest/?badge=latest)

Generic Azure function used to download Cosmotech API scenarios

The azure function allows the web-app to get the data associated to a given scenario, including parameters and datasets of types :
- Azure Digital Twin
- Cosmo Tech Twin Cache
- Storage

# Deploy the generic Azure Function App

## Pre-Requisites

- Dedicated App registration created (see details below)

### Dedicated app registration :

1. Create a new app registration
2. Add a API permission to the Cosmo Tech Platform API, choose the permission type *_Application_* (not *_Delegated_*) and select the permission *_Platform.Admin_*
3. Create a client secret
4. In the related Azure Digital Twins resources, assign the role _Azure Digital Twin Data Reader_  to app registration 



[![Deploy to Azure](https://aka.ms/deploytoazurebutton)](https://portal.azure.com/#create/Microsoft.Template/uri/https%3A%2F%2Fraw.githubusercontent.com%2FCosmo-Tech%2Fazure-function-scenario-download%2Fmain%2Fdeploy%2Fazuredeploy.json)

## Installation options

| Parameter            | Note                                                                                                                                                                                                                                       |
|----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Subscription         | Choose same as the related platform and webapp                                                                                                                                                                                             |
| Resource group       | Choose same as the related platform and webapp                                                                                                                                                                                             |
| Region               | Choose same as related platform and webapp                                                                                                                                                                                                 |
| Site Name            | Choose a name for the function app or leave the default value for auto-generated name                                                                                                                                                      |
| Storage Account Name | Choose a name for the storage account required for the function app or leave the default value for auto-generated name                                                                                                                     |
| Location             | Location for the resources to be created (Function App, App Service plan and Storage Account)                                                                                                                                              |
| Csm Api Host         | Cosmo Tech Platform API host                                                                                                                                                                                                               |
| Csm Api Scope        | Scope for accessing the Cosmo Tech Platform API (must end with /.default)                                                                                                                                                                  |
| Az Cli ID	           | Client ID of the dedicated app registration (see pre-requisites)                                                                                                                                                                           |
| Az Cli Secret        | Client Secret create of the dedicated app registration (see pre-requisites)                                                                                                                                                                |
| Package Address      | URL of the Azure function package to be deployed  - IMPORTANT : pick the URL from the latest release, ex [release 2.1.10](https://github.com/Cosmo-Tech/supplychain-azure-function-dataset-download/releases/download/2.1.10/artifact.zip) |


## Configure CORS

### Request Credentials
Check option _*Enable Access-Control-Allow-Credentials*_

### Allowed Origins :
- Add the URL of the Cosmo Tech Web-App
- For dev usage (optional) add http://localhost:3000


# Secure the Azure Function

The azure function includes a first level of securizartion with the host key.<br>
This keys being included in the web application, we need a second layer of securization by limiting the azure function calls to the users being authorized to the Cosmo Tech API 

## Add identity provider

- Go to Authentication
- Add identity provider
- Select "Microsoft"
- In "App registration type", select "Pick an existing app registration in this directory"
- Name or app ID : enter the web application name.<br>
**Note** : You may need to enter the app registration ID created for the webapp instead of its name. And in this case, you will have to create a secret for the app registration of the web app and provide it here.
<br>

- Restrict access : "Require authentication"
- Unauthenticated requests : HTTP 401
- Token store : leave checked
<br>

## Configure audience
- In the created identity provider, click on "Edit"
- Allowed token audiences : Enter the Client ID of your Cosmo Tech Platform App Registration 

## Deploy the new Azure Function version


In order to deploy the new artifact, you have to make it accessible for deployment from the azure function app instance through an https URL.

- if the build can be automated, URL can point to a GitHub release (like the generic azure function)  
Example URL : https://github.com/Cosmo-Tech/azure-function-scenario-download/releases/download/1.0.1/artifact.zip

- if not, the artifact zip file can be copied to an azure blob storage  
example URL : https://myblobstorage.blob.core.windows.net/content/artifact.zip?st=2018-02-13T09%3A48%3A00Z&se=2044-06-14T09%3A48%3A00Z&sp=rl&sv=2017-04-17&sr=b&sig=bNrVrEFzRHQB17GFJ7boEanetyJ9DGwBSV8OM3Mdh%2FM%3D

Then to deploy the new artifact version, go to the azure function app settings in the Azure portal.  
Change the `WEBSITE_RUN_FROM_PACKAGE` parameter with the new artifact URL.

Or execute the following command from the Azure CLI
```bash
az webapp config appsettings set --name <function app name> --resource-group <resource group name> --settings WEBSITE_RUN_FROM_PACKAGE=<URL>
```

**Note** : The function app automatically restarts after a configuration change.

