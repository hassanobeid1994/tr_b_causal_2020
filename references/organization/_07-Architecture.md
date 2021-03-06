---
jupyter:
  jupytext:
    formats: ipynb,md
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
      jupytext_version: 1.4.1
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

# Architecture


## 1. At a “high” level, how will the project deliver each of the needed requirements?
- **Try to think in terms of some manageable (e.g. 10-20) steps**
- **List needed intermediate products (e.g. pseudo-code, unit tests, etc.)**
- **Try to be concise but comprehensive?**

The project is split into three main tasks:

1. The first task is focused on a selection-on-observables problem:

For a causal graph with independent covariates:
 1. Ingest data
 2. Manipulate data as needed, the output of this step will be a cleaned dataset
 3. Specify and estimate a choice model based on the data at hand, the specification should follow required conventions by third party dependencies
 4. The cleaned dataset will be used in a function that estimated the distributions for variables of interest, this function will produce a parameter dictionary containing the type of variables, the best fitted distribution, and that distribution parameters.
 5. The resulting parameter dictionary from the previous step will be used to simulate needed data
 6. Based on observed availability of allternatives, a function will use the cleaned dataset to simulate an availability matrix for alternatives for the simulated dataset
 7. The specified model from step 3 will be used to simulate choices for the simulated dataset.
 8. The dataset will be used to estimate a choice model and recover the necessary parameters. These parameters can be stored in a dictionary.
 9. Steps 5-8 will be repeated for N times (say 100) and the parameters from each iteration will be stored in a dictionary entry.
 10. These paramaters will be stored in a dictionary that will be used in a function to plot the original parameters used to simulate the choices (from step 3) along with any recovered parameters from step 9.
 11. One variable will be perturbed to simulate a potential external intervention. In this scenario, no other variables will be changes since all covariates are independent.
 12. Causal effects will be estimated using the models estimated in step 3 and 9.
 13. Plots will be produced to show the distribution of "naive" and "true" causal effects


For a realistic causal graph with confounding:
Results from steps 1-3 above are reused.
 4. Specify the realistic causal graph with desired confounding structures. The causal graph will be saved as a causalgraphicalmodels object and can be saved as .png file
 5. The cleaned dataset will be used in a function that estimated the distributions for variables of interest that are nodes without any parents in the causal graph, this function will produce a parameter dictionary containing the type of variables, the best fitted distribution, and that distribution parameters.
 6. The cleaned dataset from step 2 will be used to estimate relationships between nodes in the specified causal graph from step 4.
 7. The obtained distributions from step 5 will be used to simulate data for nodes without parents in the specified causal graph.
 8. Data from step 7, alongside with estimated relationships from step 6 will be used to estimate data for the remaining nodes in the causal graph (with the exception of the utility node)
 9. Based on observed availability of allternatives, a function will use the cleaned dataset to simulate an availability matrix for alternatives for the simulated dataset
 10. The specified model from step 3 will be used to simulate choices for the simulated dataset.
 11. The dataset will be used to estimate a choice model and recover the necessary parameters. These parameters can be stored in a dictionary.
 12. Steps 7-11 will be repeated for N times (say 100) and the parameters from each iteration will be stored in a dictionary entry.
 13. These paramaters will be stored in a dictionary that will be used in a function to plot the original parameters used to simulate the choices (from step 3) along with any recovered parameters from step 9.
 14. One variable will be perturbed to simulate a potential external intervention. In this scenario, descendant children nodes of the perturbed node will also be perturbed following the estimated relationships from step 8.
 15. Causal effects will be estimated using the models estimated in step 3 and 12.
 16. Plots will be produced to show the distribution of "estimated" and "true" causal effects



## 2. Description of major components of the system and their relations:
### 2.1 What should each component do?
1. Show the need for considering the treatment assignment mechanism when estimating causal effects. This requires an application of the steps outlined in Brathwaite and Walker (2018a) to a simulated dataset from Brathwaite and Walker (2018b). This application will contain the following classes/functions:
   - Simulation functions will generate data based on any assumed causal graph (either with independent covariates or any relation between nodes)
   - Function to fit regression between different nodes from a specified causal graph
   - Function (based on pylogit) to estimate choice models based on desired specifications and specific data
   - Function to compute causal effects due to perturbation in data
Choice model estimation will try to recover the true parameters of the specified model
   - Function to plot the distribution of estimated choice model paramaters
   - Function to plot the distribution of causal effects (naive, true, and estimated)

### 2.2 What is the interface between each component and each other component?
Each component(classes) will be written to be as independent as possible from other components. Functions within classes
will depend on each other.
However, we will write functions that test the output of each of our functions to make sure we get the expected output.
In general, the interface between each of the project components will be some sort of data: dictionaries storing distribution parameters,
simulated data, estimated model parameters and causal effects, causal graphs, arrays of statistics about estimated model parameters or estimated causal effects, distribution statistics. **this list is not
comprehsive yet** Answer to question 7.6 provides a checklist of data characteristics that will be checked.

### 2.3 How do components use each other (if they do?), and which ones are allowed to use which other components?
Outputs of simulation classes/functions will be used in estimation classes/functions. 
Outputs of estimation classes/functions will be used in plotting functions.

## 3. Description of needed development / computational environment:
### 3.1  Where will development take place (virtual environments? One’s laptop, etc.)?

- There are two alternatives:
  - **Virtual Machine**: Install JupyterHub on cloud server with multiple users and the same environment for each user. Collaborate directly on the Jupyter Notebooks and convert them to Jupytext .py files for easier code review and version control.
  - **Personal laptop**: work locally on personal laptop and push changes as progress is made to the right folder in the github repository.

### 3.2  How will one reliably construct the needed computational environment?

- There are two Alternatives:
  - If using **Virtual Machine**: The created JupyterHub server will have all the dependencies installed and available to all users on the server. The server administrator will be responsible for installing necessary environment from a .yml file.
  
  - If using **personal laptop**: 
      * Create a conda virtual environment with all the necessary packages for the project, and push it to the github repository as a .yml file in order for it to be duplicated by other members and end users, **OR**
      * Create a Docker image of the computational environment to be used by all team members.

### 3.3  How will one test that the computational environment is correctly created?

- Shell commands in either situation will be used to check that the correct environment was created/installed.
- Write class/function to make sure each of the needed packages and right python version is installed.

## 4. Description of major classes to be used (relates to major components above):
<!--- **Class responsibilities**
- **Interactions between classes**
- **Class hierarchies / state transitions / object persistence**
- **Organization of classes into subsystems (if necessary / planned)**
- **Why does each class have “jurisdiction” over the parts of the system that it does?** -->

The classes are to be used in the simulation work are as follows:
 -  Class that contains functions to simulate data based on best fit distributions
 -  Class that contains functions to simulate data based on assumed causal graph
 -  Class to estimate the choice model based on specified utility equations and retrieve model statistics


## 5. Description of the minimally viable product (if any):
- **Note the portions of the architecture responsible for producing the minimally viable product.**

 - For objective 1, a minimally viable product is a notebook that takes data from outside sources and imports scripts including classes
 from question 4, calls on the functions in each of the classes to simulate data, estimate models, estimate causal effects due to an intervention, and plot distribution of obtained causal effects.

## 6. Description of algorithms:
### 6.1  What, if any, computational algorithms are being implemented as part of this project instead of relying upon external implementations?
Hassan to fill in based on the deconfounder work.

### 6.2 What purpose(s) do those algorithms serve?
See above

### 6.3 Are each of these algorithms fully understood by someone on the project team?
See above

### 6.4  What are alternative algorithms that could have served the purposes of the algorithms we are implementing?
See above

### 6.5 Why are we using the particular algorithms we’ve chosen instead of others? 
See above

### 6.6 Why do we believe the algorithms can be implemented?
See above

### 6.7 Do we have any concerns with regard to algorithmic efficiency?
See above

<!-- #region -->
## 7. Description of data usage in the system:
### 7.1 How will data be ingested / accessed?
Data will be ingested using pandas from either an online path to the dataset or from a local path on the user's machine

### 7.2 How will data be validated?
Data will be validating by reestimating the models from the Assymetric paper by Brathwaite and Walker.

### 7.3 How will data be organized?
Data will be organized in tabular format (.csv)

### 7.4 How will data be transformed?
Data will be transformed using methods available within Pandas

### 7.5 How will created data be output and stored?
Causal graphs will be output to .png files and pushed to the repo

Summaries of model estimate will be saved as markdown tables

Plots of results will be saved as .png files and pushed to the repo and included in the final presentation

Previously estimated models will be stored in a dictionary that can be pickled and loaded later.
### 7.6 How will created data be validated?
The simulated data will be validated as follows:
- Ensure we have all the columns we expect
- Ensure all columns have the correct tyoes
- Ensure all numeric columns have the expected ranges
- Ensure the numeric columns having the means and variances within expected ranges
- Ensure we have the correct number of observations

This will be achieved by writing a function running all assertions needed.


### 7.7 How does all of the above differ online vs offline? (e.g. we may throw a critical error offline to prevent training with bad data but only log a warning online to note that the data in a request was unexpected.)
N/A

### 7.8 How will the flow / manipulation of data be controlled (and recorded / version-controlled) and made reproducible? E.g. data ingestion and manipulation to create training / testing sets.
- **Flyte?**
- **Make?**
- **Other?**  
Developing a project workflow file that shows how all specified requirements of each workflow
step are met. 

## 8. Description of experimentation protocols (if relevant):
**If experiments need to be run (e.g. hyper-parameter tuning, model-selection, A/B tests, etc.):**
### 8.1 How will experiments be launched?
We can launch the experiment from a jupyter notebook, and **hopefully** from the command line.

### 8.2 How will experiment reproducibility be ensured?
Simulated data, as well as any experiment output will be store either in csv/json/pickle file
based on the nature of the object (dataset, model, etc..) and will be loaded into a notebook.
A third party library called `sacred` can be used https://sacred.readthedocs.io/en/stable/
Setting seed parameters in our functions will also be helpful in reproducing the results of our experiments.

### 8.3 How will experiment meta-data (e.g. launch configurations) be stored?
The meta-data for the experiment could be stored in a requirements.txt, the source code,
and parameters stored in a .json/pickle/csv file. the sacred library has a `run` object
that stores all experiment info and configuration.

### 8.4 How will experiment-created data (e.g. results) be stored?
The experiment-created data will be stored in json/pickle/csv files.

### 8.5 How will experiment-created data be analyzed?
Experiment metrics will be analyzed to find statistics about means and variances of parameters
to make sure they fall within the expected ranges.

### 8.6 How will experiment analyses be prepared for public reporting? 
Experiment analyses will be stored in .json/csv files and used to create plots summarizing
results of the experiments.

## 9. Description of user-interface:
### 9.1 How will users (including myself) interact with the system that is built?
- **Will there be a command line interface?**
- **Will users be editing configuration files, and if so, where will they be stored?**
- **Will there be ability to replay the DAG representing one’s data analysis?**

Users will use a jupyter notebook to interact with the system. The `papermill` library
will be used to parametrize a notebook. Parameters of the notebook could also be saved
in a .json file that is loaded into the notebook. For experiments, the `sacred` library
will help in storing experiment paramters.

### 9.2 How will ease of changes be ensured (e.g. changing a given hyperparameter value in the source code of a model)?
Each hyperparameter that needs to be tuned will be included in the parameter definition of a function. Users will be
able to change these parameters directly from the notebook running the functions of interest. These parameters will be set as initial global notebook variables than can be easily changed by the users.

### 9.3 Is the user-interface self-contained so that other parts of the system are insulated from changes in the user-interface?
Yes. Users will not be able to make any changes to the source code by interacting with the notebook.

## 10. Description of resource-management:
### 10.1 How will the system cope with large amounts of data during model training?
The system will not have to deal with large amounts of data that personal laptops will not be able to handle.

### 10.2 How much memory and time will it take the system to execute?
- **Offline / online prediction**
- **Model training**
Any personal laptop should be able to execute the system. We don't envision the need for large memory requirements.
It is unknown exactly how long it will take the system to run, but the objective is to have each sub-system take as little time as possible.
As of now, the notebook representing the deliverable for objective 1 of the project runs in 20 minutes for 400 simulations. This time can be further reduced by refactoring the current functions responsible for achieving the objective of the notebook.

### 10.3 How will the system interact with the external world to acquire resources? (e.g. get data or spawn virtual machines
We can access data directly from a specified weblink or path for the dataset within the established repo. relative paths using APIs if necessary can be set in the notebooks to make this happen.

#### 10.3.1 How does the system decide how much of an external resource is needed? (e.g. how many virtual CPUs are required during training?) 
N/A

## 11. Description of how the system will scale:
### 11.1 With increasing dataset sizes: 
There is no current plan for scaling the system to adapt to large datasets.

### 11.2 With increasing numbers of models being used:
The number of models used should not affect the scalability of the project.

### 11.3 With increasing numbers of parameters:
N/A

### 11.4 With increasing numbers of divergences/losses:
N/A

## 12. Description of how the system will interface with external systems:
- **E.g. if a model needs to be served in Go but it was trained in Python…**
- **If the system needs to manipulate Kubernetes for training...**

N/A

## 13. Description of how errors will be handled:
### 13.1 What are common expected errors from users and how can we guard against them?
Having a wrong specification for a desired model, pylogit has built-in mechanisms to guard against it
Having the wrong parameters or wrong parameter format in each of the functions/classes used in the project. Detailed docstrings will be used to help users figure out the needed parameters in each function along with their format. The initial parameter initialization will also help users see example use cases of the functions.
### 13.2 Will we try to fix errors or merely notify users of the error’s presence?
We will only notify users of the error's presence.

### 13.3 When errors are encountered, will we quit immediately or wait until some specified point before notifying users of errors? For which errors is each strategy appropriate?
Quit immediately in the case of all errors.

### 13.4 What are the conventions for error messages that the system reports?
No specific convention is set.
<!-- #endregion -->

### 13.5 Where are errors processed? At the point of detection, by a central error handling class, by functions above in the call stack, etc.
Errors are processed at the point of detection.

### 13.6 What level of responsibility does each class have in validating its own input? Is there a central class (or set of classes) that performs all validation? When can classes assume clean information?
Code for input validation can be built in separate functions and be used part of analysis functions as seen needed.

### 13.7 How will we use (or not use) type hinting to help prevent errors?
Docstrings will suggest to the users what each of the function takes in as types and what it returns.
`mypy` is an additional option to be used for type hinting withing each of the functions.

## 14. Description of testing plan:
### 14.1 How will we test that all of the parts of the architecture are working correctly?
- **How will we create tests for each part of the architecture that are:**
 - **clear and unambiguous**
 - **capable of dealing with stochastic functions / objects**
 - **minimizing reliance / use of stochasticity**
 - **fast to evaluate**

The first thing that comes to mind is running the same tests (probably using `hypothesis`?)
many times and then verify that the output statistics match one's expectations. In order for tests to be fast, each
test will need to focus on one functionality. We can have docstrings/clear names explaining what each test function is doing (the naming convention in pytest makes this easy). Each test should also be independent from other tests.

### 14.2 What are the various types of tests that are needed?
Unit tests/Feature tests, integration tests.

### 14.3 Are there any parts of the architecture that we do not know how to test? How will these knowledge gaps be resolved before the coding begins?
Given our preliminary knowledge on testing, there will be elements that we won't know how to test. 
Reading through available documentation and tutorials for pytest or other packages will help resolve any knowledge gaps 
in testing any of the parts of the architecture.

### 14.4 How will discovered bugs be turned into test cases?
The guide provided by Timothy on how to debug code will be followed to move from finding the bug to testing it.

### 14.5 How will the software be reviewed in general (beyond automated tests) to reduce the probability of programming bugs into the code / increase the chance of producing correctly functioning software?
Cross-review between team members will help in detecting any bugs or any testing gaps.

## 15. Description of project-sharing procedures:
### 15.1 Is there a plan in place for producing documentation for the software?
- **Documentation for operating the software**
- **Documentation of software limits**
- **Usage examples and tutorials**
- **Key project learnings / retrospective notes**

Documentation, in the form of Jupyter Notebook accompanied by a Markdown file (README.md) detailing the procedure for installing the environment and the content of folders and notebooks. Any limitations to the project will be noted in the jupyter notebooks developed to illustrate the analysis effort. The README.md markdown file will also will point to documentation pages for any packages used in the project.

For each of the functions and classes written for this project, we will write detailed docstrings that help with how the functions
and classes function and what they output.

### 15.2 Is there a plan for sharing the software with others?
- **File upload?**
- **Upload to package repository?**

All project related material including code, documentation, presentation, environment files, and datasets will be uploaded to the project github repository.

### 15.3 Will the project have an associated website? If so is there a plan for its development?
The only "website" for the project will be its github repository.

### 15.4 Is there a plan for producing any written or visual materials that others may wish to view?
- **Final or interim project reports**
- **Tables of key project results**
- **Graphs, diagrams, images from the project, e.g.:**
 - **Plots of system performance**
 - **Model checking plots**
 
**This was directly taken from the requirements document**

1. Public notebooks
   1. Selection-on-observables simulation:
      - How are our causal effect estimates impacted by using an incorrect causal graph, in the simplest and most ideal setting?
   2. Deconfounder demonstration with data from Brathwaite and Walker's asymmetric models paper.
      - Does the deconfounder approach substantially change the estimated causal effects and inferred sensititivities?
   3. Deconfounder investigation based on simplified simulations
      - What are the potential pitfalls of the deconfounder approach? How can we look out for them?
   4. Deconfounder demonstration using realistically simulated data based on data in Brathwaite and Walkders asymmetric models paper.
      - Are our results obtained with the real data qualitatively consistent with results obtained on realistically simulated data that we know satisfy the deconfounders assumptions?
   5. Demonstration of falsification techniques.
      - How can we test the assumptions underlying our proposed / hypothesized causal graphs?
2. Resulting plots / tables
   - Selection-on-observables simulation
      - Correctly estimated vs True causal effect of travel distance reduction on automobile mode shares (drive alone + shared_ride_2 + shared_ride_3+).
      - Naively estimated vs True causal effect of travel distance reduction on automobile mode shares (drive alone + shared_ride_2 + shared_ride_3+).
   - Simplified / Illustrative Deconfounder simulations
      - Plots of misleading p-value conclusions when using posterior predictive checks.
      - Plots of alternative posterior predictive checks of the factor model for one's deconfounder.
      - Plots of the relationship between confounder inference error and outcome model parameter bias.
   - Deconfounder demonstration with real data
      - Plots of asymptotic distributions of model coefficients with and without the inferred deconfounders.
      - Plots of predicted distributions (based on the asymptotic distribution of model coefficients) of causal effects with and without the inferred deconfounders.
   - Deconfounder demonstration with realistically simulated data.
      - Plots of asymptotic distributions of model coefficients with and without the inferred deconfounders.
      - Plots of predicted distributions (based on the asymptotic distribution of model coefficients) of causal effects with and without the inferred deconfounders.
      - Comparison of the two plots above next to those same plots based on the real data.  
      We want to know if the results observed using the real data are qualitatively consistent with the results obtained using data that we know satisfies the deconfounder assumptions.
   - Falsification tests
      - Causal graph for Utility Drive Alone.
      - Marginal independence test statistic distribution vs observed value, for causal graph of Utility Drive Alone graph.
      - Conditional independence test statistic distribution vs observed value, for causal graph of Utility Drive Alone graph.
      - Deconfounder causal graph for Utility Drive Alone
      - Prior and posterior predictive test statistic distribution for conditional independence test statistics vs observed test statistic value.
3. Supporting source code.
   - Selection-on-observables
      - Function(s) for estimating some statistical model for each treatment node given its parents.
      - Function for simulating data from a specified causal graph, the estimated statistical models of each treatment node given its parents, and a given outcome model given the treatment nodes.
      - Function for re-estimating a given outcome model, conditional on a set of simulated data for the parents of the outcome nodes.
      - Function for estimating causal effects given a specified causal graph and relationships between  nodes and their parents.
      - Function for plotting the distributions of estimated causal effects under various causal graphs and relationships between nodes and their parents.

   - Deconfounder
      - Function for fitting factor model  
        A class with a few of factor model methods:  
        Probabilistic PCA, Deep exponential family, Poisson Matrix Factorization?
          1. Inputs:
             - Matrix of covariates
             - Dimensionality of latent variable space
             - Type of factor model to be estimated
          2. Output: A fitted factor model
      - Function for prior predictive checks of the factor models.
         1. Inputs:
            - Factor model
            - Training data
            - Prior distributions of factor model parameters
         2. Outputs: P-values and plots for predictive checks
      - Function for posterior predictive checks for the factor models.  
         1. Inputs:
            - Factor model
            - Training and/or testing data
            - Posterior distributions of factor model parameters
          2. Output: P-values and plots for predictive checks
   - Falsification of causal graphs
      - Function for marginal independence tests
      - Function for conditional independence tests
      - Function for prior/posterior predictive conditional independence tests
4. Tests for all source code and notebooks.
   1. [At Minimum] Integration tests of public notebooks.
   2. [At Minimum] Unit tests of all critical / top-level / non-trivial / non-standard functions.
   3. [Ideally] Unit tests of all source code.

## 16 Description of maintenance plan:
### 16.1 How will the system / software be maintained after initial creation?

The source code of the project will be improved/expanded by adding more capabilities as needed.

### 16.2 What needs to be done for maintenance?
The source code for any functions/classes will be modified following the github workflow. One will submit an issue showing the bug/need for extension with a minimal working example or desired output, followed by a pull request with fixed code or added features. The pull request will be merged once code is reviewed by team. Refactoring will make this process easier as it will be smoother to isolate the issue and make any needed extensions of functionality. 

### 16.3 Who will perform needed maintenance activities?
Hassan/Amine, and other interested students in Joan's group.

## 17. Description of project tools:
### 17.1 What are all the tools and major external systems upon which the project depends?
Standard scientific packages such as: numpy, pandas, scipy, pylogit, causalgraphicalmodels(or others),
seaborn/matplotlib, scikitlearn, pyro, fitter, pytest. This list is not exhaustive and could grow.

### 17.2 Is there evidence that we understand the basics of how all of those tools work?
- **Have we read any/all relevant documentation and instruction materials?**
- **Have we taken any basic training courses in any of these tools?**

Each team members is individually familiar working with the majority of these packages. Collectively, the team is
familiar working with all of these packages. If additional packages are needed and no team member has the expertise
needed to work with them, the team will make sure to read any available documentation or use examples available. 

## 18. Description of project risks and mitigation efforts:
### 18.1  There should be some evidence for, and of, project feasibility:
- **How do we know that every part of the architecture will work?**
- **Based on the architecture, what are all needed resources?**

The architecture is mainly based on third party dependencies that have proven to work. The needed resources will be
one's laptop with an installed environments/requirements and compatible python version. For any functions/classes developed as part of this project, we will write tests that will ensure that we get the expected outputs.

### 18.2 What could render the project infeasible?
- **Is there adequate resourcing?**

We do not envision inadequate resourcing problems to occur.

### 18.3 Are there known sources of difficulty based on the planned tasks?
The sources of difficulty are related to learning proper software engineering practices and learning about new
third party dependencies. Additionally, getting comfortable with some of the methods used in the project has proven to be a roadblock at times.

### 18.4 Are there mismatches between prior knowledge and required tasks?
Yes, this is mitigated by reading literature on methods to be used, or documentation of python or any third party dependencies used in the project.

### 18.5 What are the weakest areas of the architecture?
- **Where is the project most vulnerable to failure?**
- **How are these weaknesses being addressed?**
At this moment, the weakest areas of the architecture are as follows:
- The lack of tests in the available code and the lack of refactoring that could make it hard for use by other outside users.
- The lack of a project workflow file to enable reproduction of the final results. I think this one will be fairly 
  straightforward to make, assuming we follow good practices of creating modular notebooks and code. **(Currently in progress)**
- The lack of a reproducible experiment system. We have no way to track all the different ideas that are likely about 
  to be tried in the next month to get final results. Afterwards, we will then be unable/less-able to reproduce our work
  along the way to the final results. As a result, we'll be unable/less-able to harvest any useful information from this
  period since it's more difficult to use the knowledge of what didn't work if you don't remember all the things that didn't work.

## 19. Description of the approach to over-engineering:
### To what extent should planning be done to prevent all errors versus to produce the simplest system necessitated by the requirements?
Planning should be done at incremental levels to avoid missing any potential error when planning for a large system.
Planning could be done at the function/small task level for example.

## 20.  Description of change strategy:
### 20.1 What steps are being taken to ensure that the architecture is able to handle changes with maximal ease / flexibility? e.g.:
- **Newly desired capabilities based on usage of initial iterations**
- **Adding planned features that didn’t make it to the minimal viable product**
- **Allowing for easy change of third party dependencies**
- **Complying with any relevant standards for maximal compatibility with outside products**
- **New ways of interaction with users (e.g. avoiding type checking as much as possible in favor of duck-typing)**
- **Are classes maximally independent such that changes in one class don’t necessitate changes in the others?**
- **Do we have a plan in place for test changes? For example if needing to change the data used in a test, can that be easily done without having to rewrite the test? E.g. data stored outside the code, or integration tests that don’t test for a specific prediction output but rather a property of the prediction outputs so that the model can change without the test necessitating a rewrite.**

The team members will write functions and classes that are as independent as possible to make changes easy to implement.
Tests will be rewritten accordingly.

The source code will be refactored and will comply with PEP8 for easier readability for new users and contributors. 

We have no currently established plan for ease of change of third party dependencies.

### 20.2 What is the strategy for handling requests for new features from or updates of the system after its built?
Issues will be posted to the github repository and assigned to one of the team members. The team member will add
the requested feature and submit a pull request for review by other team members. Once the review process is over, the 
change and new feature can be merged to the master branch.

### 20.3 How will bug-fixes be handled? By whom?
Bug fixes will be prioritized based on importance and urgency. Each bug fix will be handled by a team member most
comfortable with the source code for the sake of efficiency. The debugging code shared by Timothy will be key in fixing any bugs in the code. Fixing bugs will also follow the github workflow starting with submitting an issue and creating a branch for fixing the bug, all the way until merging the branch to `master`.

## 21.  Description of reuse strategy:
### How is the architecture maximally leveraging previously completed work?
The architecture makes uses of many third party dependencies for data ingestion, data processing, analysis, and 
producing output. The team members are trying to write as little new code that replicates existing functionality 
as possible.

## 22. Description of architectural alternatives (i.e. alternatives to how to carry out the project):
### 22.1 What are the closest alternative systems that could be used for this project or for parts of the project?
- **How can those alternate systems be leveraged?**

We are unaware of any alternative systems that accomplish exactly what we would like to accomplish in this project.

### 22.2 Why is it expected that this project’s custom built sub-systems will be better than the available alternatives for those sub-systems?

We are unaware of any available alternatives for any of the required tasks in this project.

## 23. Description of architectural alternatives (i.e. alternatives to how to carry out the project):
### 23.1 What were alternative ways to architect the system to satisfy the requirements?
- **If there were no other alternatives, then why were there no other alternatives and can we prove this was really the case?**

No transportation researchers have addressed the problems we are tackling in this project, to our best knowledge.
We can not prove that no alternatives exist.

### 23.2 Why did we choose to architect the system the way we did?

- What were our objectives in choosing the given architecture?
- What were the motivations for all major decisions?

The architecture was incrementally designed to respond to evolving project objectives. The main objective is to design the architecture in a way that satisfied the project objectives and makes the code easily reusable and extensible for any user who has a basic knowledge of Python. Additionally, we want to make it provide the three deliverables needed for the project.

## 24. Description of expected debugging protocol:
### Should detail the expected debugging process to be used when, despite all of our planning and checking, failure is experienced while using some piece of the implemented architecture.
The debugging protocol to be followed was outlined by Timothy and is available as one of the references in the repo.
## 25. Final checks:
### Do any parts of the system seem over- or under-architected. Empirically, are the descriptions of any sub-component much more thorough than any other?
All the subsystems right now aim to deliver the minimum viable product. This means that these systems could be
under-architected. This will be adjusted as more insight is gained about how the different pieces of the system should
function interactively.
