Make a simple Image  #1
Lets build a very simple image using the linux fun tool cowsay, push it to Docker Hub, and then Moo a container using that image.

Creating and running our first Image
In order to save your "Magic Commands" and be able to replicate the same Enviroment we need a image. 
An Image is best created and maintained using a Dockerfile.
This file acts as an instrcution for Docker Engine to know how to build the image. 

In your console, create a folder named cowsay_yourname.

In this directory, create a create a file named Dockerfile
In the file, put the following:




What does these mean :
The FROM command tells the builder that our container image will base from the ubuntu image. 
Any instructions performed after this will create more layers in this image.
The RUN command will update and install cowsay 
The ENTRYPOINT instruction allows you to configure a container that will run as an executable. It looks similar to CMD, because it also allows you to specify a command with parameters 
The CMD instruction allows us to set a default command, which will be executed only when you run container without specifying a command. 
If Docker container runs with a command, the default command will be ignored


At this point, let's build our image! Run the following command:

docker build -t my-fun-cowsay .
The -t flag indicates a 'tag', or a name that we want to apply to the image. We can then use that to start a container from that name (which we'll do next).
The trailing . tells the Docker Engine that the Dockerfile and build context to be used is the current directory. The build context indicates the root of files we will use in the Dockerfile (like the copying of the index.php file).
Let's run our container image! Run the following command:

docker run my-fun-cowsay

Congrats! You've now created and run your first container image!

Sharing the Image
The image you just created exists only on the machine that performed the build. So, if we want to share the image, we need to push it to a registry. Think of a registry as a code repo. It's sole purpose is to share container images.
In order to push to Docker Hub, we need to authenticate. Do this by running:

docker login
All images (except Official Images) in Docker Hub are namespaced. For example, if I push images, they aren't going to simply named my-first-php-image, as it doesn't convey who it comes from, but creates a nightmare trying to ensure my image doesn't collide with yours. To fix this, my image would be named mikesir87/my-first-php-image. Using the docker tag command, we can provide another name for the image we built earlier.

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

Wrap-up
While this was a pretty simple application, let's think about what was needed to run the application.

We needed a PHP runtime engine, an Apache HTTP server, and a PHP script. Before containers, we would have needed to have a machine that had the correct versions installed and make the script available. 
But, our container image shipped everything it needed to run.
We created our container image using a Dockerfile, which assures our application is consistent no matter where we build it. 
With it being a text file, the full environment of our application can be version controlled!
