
// -------------------------------------------------------- //
// Parameters
// -------------------------------------------------------- //

param location string

param tags object

param storageAccountName string

@description('SKU name for storage account')
param storageSku string

// -------------------------------------------------------- //
// New resources
// -------------------------------------------------------- //

resource storageAccount 'Microsoft.Storage/storageAccounts@2023-01-01' = {
  name: storageAccountName
  location: location
  tags: tags
  sku: {
    name: storageSku
  }
  kind: 'StorageV2'
}

// -------------------------------------------------------- //
// Output
// -------------------------------------------------------- //

output Id string = storageAccount.id
output storageAccountName string = storageAccount.name
