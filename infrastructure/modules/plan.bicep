
// -------------------------------------------------------- //
// Parameters
// -------------------------------------------------------- //

param projectName string

param location string

param tags object

param skuName string

param planSkuTier string


// -------------------------------------------------------- //
// Variables
// -------------------------------------------------------- //

var appServicePlanName = 'plan-${projectName}-01'

// -------------------------------------------------------- //
// New resources
// -------------------------------------------------------- //

resource plan 'Microsoft.Web/serverfarms@2022-09-01' = {
  name: appServicePlanName
  location: location
  kind: 'linux'
  tags: tags
  sku: {
    name: skuName
    tier: planSkuTier
  }
}

// -------------------------------------------------------- //
// Outputs
// -------------------------------------------------------- //

output planId string = plan.id
output PlanName string = appServicePlanName
