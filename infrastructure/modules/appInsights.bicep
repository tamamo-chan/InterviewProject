
// -------------------------------------------------------- //
// Parameters
// -------------------------------------------------------- //

param projectName string

param location string

param tags object

// -------------------------------------------------------- //
// Variables
// -------------------------------------------------------- //

var appInsightsName = 'appi-${projectName}-01'

// -------------------------------------------------------- //
// New resources
// -------------------------------------------------------- //

resource appInsights 'Microsoft.Insights/components@2020-02-02' = {
  name: appInsightsName
  location: location
  tags: tags
  kind: 'web'
  properties: {
    Application_Type: 'web'
    publicNetworkAccessForIngestion: 'Enabled'
    publicNetworkAccessForQuery: 'Enabled'
  }
}

// -------------------------------------------------------- //
// Outputs
// -------------------------------------------------------- //

output Id string = appInsights.id
output name string = appInsightsName
