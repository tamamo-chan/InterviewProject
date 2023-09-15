
// -------------------------------------------------------- //
// Parameters
// -------------------------------------------------------- //

@description('Application insights name')
param appInsightsName string

@description('App Service Plan name')
param planName string

@description('Storage account name')
param storageAccountName string

@description('Subnet name')
param subnetName string

param projectName string

param location string

param tags object


// -------------------------------------------------------- //
// Variables
// -------------------------------------------------------- //

var functionAppName = 'fn-${projectName}-01'
var azureWebJobsStorage = 'DefaultEndpointsProtocol=https;AccountName=${storageAccount.name};privatelink;EndpointSuffix=${environment().suffixes.storage};AccountKey=${listKeys(storageAccount.id, storageAccount.apiVersion).keys[0].value}'

// -------------------------------------------------------- //
// Existing resources
// -------------------------------------------------------- //

resource appInsights 'Microsoft.Insights/components@2020-02-02' existing = {
  name: appInsightsName
}

resource plan 'Microsoft.Web/serverfarms@2022-09-01' existing = {
  name: planName
}

resource storageAccount 'Microsoft.Storage/storageAccounts@2023-01-01' existing = {
  name: storageAccountName
}

resource subnet 'Microsoft.Network/virtualNetworks/subnets@2023-05-01' existing = {
  name: subnetName
}



// -------------------------------------------------------- //
// New resources
// -------------------------------------------------------- //

resource functionApp 'Microsoft.Web/sites@2022-09-01' = {
  name: functionAppName
  location: location
  tags: tags
  kind: 'functionApp,linux'
  properties: {
    virtualNetworkSubnetId: subnet.id
    enabled: true
    serverFarmId: plan.id
    appSettings: [
      {
        name: 'AzureWebJobsStorage'
        value: azureWebJobsStorage
      }
      {
        name: 'APPINSIGHTS_INSTRUMENTATIONKEY'
        value: appInsights.properties.InstrumentationKey
      }
      {
        name: 'APPLICATIONINSIGHTS_CONNECTION_STRING'
        value: 'InstrumentationKey=${appInsights.properties.InstrumentationKey}'
      }
      {
        name: 'FUNCTIONS_EXTENSION_VERSION'
        value: '~4'
      }
      {
        name: 'FUNCTIONS_WORKER_RUNTIME'
        value: 'python'
      }
    ]
  }
}

// -------------------------------------------------------- //
// Outputs
// -------------------------------------------------------- //

output Id string = functionApp.id
output name string = functionAppName
