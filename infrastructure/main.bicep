// -------------------------------------------------------- //
// Parameters
// -------------------------------------------------------- //

param location string

param tags object

param skuName string

param skuTier string

param storageSkuName string


// -------------------------------------------------------- //
// Network
// -------------------------------------------------------- //

@description('Specific subnet name in the Vnet')
param subnetName string

// -------------------------------------------------------- //
// Variables
// -------------------------------------------------------- //

var projectName = 'interview-project'
var storageAccountName = 'st${projectName}${uniqueString(resourceGroup().id)}'

// -------------------------------------------------------- //
// Resources
// -------------------------------------------------------- //

module appInsights 'modules/appInsights.bicep' = {
  name: 'appInsights_${projectName}'
  params: {
    location: location
    projectName: projectName
    tags: tags
  }
}

module plan 'modules/plan.bicep' = {
  name: 'plan_${projectName}'
  params: {
    location: location
    planSkuTier: skuTier
    projectName: projectName
    skuName: skuName
    tags: tags
  }
}

module storageAccount 'modules/storageAccount.bicep' = {
  name: 'storageAccount_${projectName}'
  params: {
    location: location
    storageAccountName: storageAccountName 
    storageSku: storageSkuName
    tags: tags
  }
}

module functionApp 'modules/genericFunctionApp.bicep' = {
  name: 'functionApp_${projectName}'
  params: {
    appInsightsName: appInsights.outputs.name
    location: location
    tags: tags
    planName: plan.outputs.PlanName
    projectName: projectName
    storageAccountName: storageAccount.outputs.storageAccountName
    subnetName: subnetName
  }
}









