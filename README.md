This is the visualization tool created for course CS-E4450 - Explorative Information Visualization. The project was about energy consumption and production in Finland. To run this project on your local machine do the following steps:
1. Make sure you have the latest docker desktop downloaded to your computer and that it is running
2. Open in the command line (or other similar tool) the root folder of this project
3. run the code snippet `docker compose up --build` to build the solution and start the docker container. Depending on your computer this can take several minutes.
4. open the location http://localhost:5006/visualization_with_param in your web browser to see and interact with the visualization
5. To close the visualization, open another command line (or similar tool) in this project root folder and run `docker compose down`