# Format description of the ScenarioDownload Azure Function

```json
// Description of the content
{
  "datasets": {
    "dataset_id": {
      "name": "Name of the dataset",
      "type": "Type of the dataset",
      "content": "Content of the dataset"
    }
  },
  "parameters": {
    "parameter_name": "value",
    "dataset_parameter_name": "dataset_id"
  }
}
```

## Datasets
This section will contain every downloaded datasets tied to the scenario.

The complete list of datasets is made of the datasets tied to the scenario in the "Datasets" part 
of the scenario in the API, and every parameter of type "%DATASETID%".

Each dataset is then downloaded and made available in the following format

### Dataset format
#### name
This section contains the name of the dataset, this name is the name defined in the API for the given dataset.

#### type
This section contains the type of the dataset, it can be either `adt` if the dataset is a download of 
an Azure Digital Twin instance, or it will be the file type of the file associated to the dataset.

#### content
This section will contain the full content of the dataset, depending on the type it can have multiple formats 
which will be detailed in the Content Format section.

### Content format
#### Azure Digital Twin
```json
{
  "TwinType": [
    {
      "id": "ID of the twin in ADT",
      "Property1": "Value of the Property1 of the twin",
      ...
    },
    ...
  ],
  "RelationshipType": [
    {
      "id": "ID of the relation in ADT",
      "source": "ID of the source twin",
      "target": "ID of the target twin",
      "Property1": "Value of the Property1 of the relationship",
      ...
    },
    ...
  ],
  ...
}
```
Each twin will be fully downloaded and stored in a group corresponding to its type.
The type of a twin is determined by reading the `$metadata.$model` property of the twin.

Each relationship will also be fully downloaded and stored in a group corresponding to its type.
The type of a relationship is determined by reading the `$relationshipName` property of the relationship.

Before being returned every remaining property starting with `$` will be purged from the results.

#### CSV
```json
{
  "Filename": [
    {
      "Column1": "Value of column1 for line 1",
      "Column2": "Value of column2 for line 1",
      ...
    },
    {
      "Column1": "Value of column1 for line 2",
      "Column2": "Value of column2 for line 2",
      ...
    },
    ...
  ]
}
```
The CSV file will be read and each line will be converted to a json object.

#### xls/xlsx
```json
{
  "Sheet1": [
    {
      "Column1": "Value of column1 for line 1",
      "Column2": "Value of column2 for line 1",
      ...
    },
    {
      "Column1": "Value of column1 for line 2",
      "Column2": "Value of column2 for line 2",
      ...
    },
    ...
  ],
  "Sheet2": [
    ...
  ],
  ...
}
```
An xls/xlsx file will be read as if each sheet was a single csv file. Each sheet is then returned as a list of json objects.

#### json
A json file will be sent as-is in the result.  

#### Others
If the file is not of one of the previous type, its content is put as pure text in the response in place of a constructed json object.

## Parameters
All the parameters of the scenario will be downloaded and displayed in this category.

Parameters of type `%DATASETID%` will have their value pointing to the id of the dataset which will be displayed in the `datasets` section of the output.