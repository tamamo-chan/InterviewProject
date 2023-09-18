# InterviewProject

This project provides a solution to 3/4 questions of the case study: Builder Catalogue Challenge

It provides a solution to the following questions: 

* Which sets can the user brickfan35 build with their exisiting inventory of pieces?
* The user landscape-artist doesn't have the right pieces to build the set tropical-island but would like to collaborate with other users on the build. Which users could they combine their collection with to have the complete piece requirements for the build?1
* (HARD) The user dr_crocodile wants to expand the number of sets they can build with their current inventory and are prepared to be flexible on the colour scheme. They are happy to substitute any colour in a set as long as all the pieces of that colour are substituted, and that the new colour isn't used elsewhere in the set. For example, a building with white walls, a red roof and a green flag could be built with red walls, a blue roof and a green flag. What new sets can dr_crocodile build by allowing colour substitutions?

Individual solutions are based on the username of the questions. 
Aside solving above questions, an HTTP-triggered API was also built around the first question. Furthermore, an example of an Azure DevOps pipeline and Infrastructure as Code (IaC) was added to stub deploying the API to an Azure Function App.

The following question was not included in this project: 
* The user megabuilder99 is interested in creating a new custom build but they want to make sure other people could complete it with their current inventories. What is the largest collection of pieces they should restrict themselves to if they want to ensure that at least 50% of other users could complete the build?

## Dependencies

The project was tested on Python 3.9.13. The required packages can be found in `requirements.txt`. 

For running the API locally, you need Visual Studio Code and their Azure Functions extension installed. Furthermore, you need [Azure Functions Core Tools](https://github.com/Azure/azure-functions-core-tools#installing) installed.


## How to run

To run an individual solution, you navigate to the root of the project and run the following in a console:

`python brickfan35.py`

To run all solutions:

`python main.py`

To run the API locally, navigate to the `BuildableSets/__init__.py` file and press F5. Once it is done loading, you should be able to access the API using the following link:

`http://localhost:7071/api/BuildableSets?username=brickfan35`