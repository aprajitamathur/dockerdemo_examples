# The docker file 
It  is used to build the image for running selenium in chrome and with python . This is build and saved as selenium_docker_python
# One selenium test 
The test is located in the test_python.py 
# To execute 
docker run -it  -v $(pwd):/usr/workspace aprajitamathur/selenium_docker_python test_python.py 
