Make a simple Image  #1
Lets build a very simple image using the linux fun tool cowsay, push it to Docker Hub, and then Moo a container using that image.

Creating and running our first Image
In order to save your "Magic Commands" and be able to replicate the same Enviroment we need a image. 
An Image is best created and maintained using a Dockerfile.
This file acts as an instrcution for Docker Engine to know how to build the image. 

In your console, create a folder named cowsay_yourname.

In this directory, create a create a file named Dockerfile
In the file, put the following:
FROM ubuntu
RUN apt-get update && apt-get install -y cowsay 
ENTRYPOINT ["/usr/games/cowsay"]
CMD ["Moo Moo"]

What does these mean :
The FROM command tells the builder that our container image will base from the ubuntu image.   
Any instructions performed after this will create more layers in this image.  
The RUN command will update and install cowsay   
The ENTRYPOINT instruction allows you to configure a container that will run as an executable. 
It looks similar to CMD, because it also allows you to specify a command with parameters 
The CMD instruction allows us to set a default command, which will be executed only when you run container without specifying a command. 
If Docker container runs with a command, the default command will be ignored


At this point, let's build our image! Run the following command:

docker build -t my-fun-cowsay .
The -t flag indicates a 'tag', or a name that we want to apply to the image. We can then use that to start a container from that name (which we'll do next).
The trailing . tells the Docker Engine that the Dockerfile and build context to be used is the current directory. The build context indicates the root of files we will use in the Dockerfile (like the copying of the index.php file).
Let's run our container image! Run the following command:

docker run my-fun-cowsay

Moo Moo ! We create and ran our very own first image!

Sharing the Image
The image you just created exists only on the machine that performed the build. So, if we want to share the image, we need to push it to a registry. Think of a registry as a code repo. It's sole purpose is to share container images.
In order to push to Docker Hub, we need to authenticate. Do this by running:

docker login
All images (except Official Images) in Docker Hub are namespaced (ie it includes your name in front of it to avoid confusion)

# Replace aprajitamathur with your Docker Hub username
docker tag my-fun-cowsay aprajitamathur/my-fun-cowsay
Now that we're authenticated and we have our image tagged correctly, let's push it!

# Replace aprajitamathur with your Docker Hub username

docker push aprajitamathur/my-fun-cowsay
Open your browser to Docker Hub and you should see the new repo! Feel free to click on it and see the "Pushed X minutes ago."

Running our Image

In the terminal run the following:

# Replace aprajitamathur with your Docker Hub username
docker run aprajitamathur/my-fun-cowsay STARWEST
We'll see the image get pulled from Docker Hub and start up. Magic, huh?

#Summary
We needed a ubuntu system,cowsay package, and a simple way to execute the cowsay command. 
Before docker contriners , this would take several tries before it worked. 
We needed to have a machine that had everything installed and instructions on how to run cowsay on that system.  
But, our image shipped everything anyone needs to run this out of the box .
