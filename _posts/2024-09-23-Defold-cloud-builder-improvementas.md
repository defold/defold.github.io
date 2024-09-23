---
layout: post
title:  Defold cloud builder improvements
excerpt: We are happy to announce that we've finished a large overhaul of the build servers to simplify development, maintenance and the setup of local build servers.
author: Björn Ritzl
tags: ["news", "gcp", "extender"]
---

When the Defold extension system and the cloud builders were launched eight years ago it marked a milestone for Defold when game developers no longer had to rely on the Defold development team to provide integrations to third party services and platform specific features. Instead developers could write native code and add Lua bindings and have the code seamlessly integrated into the engine without installing any additional tools or SDKs. 

The release of the extension system has resulted in a large ecosystem of plugins, available from the [Asset Portal](/assets) and integrated into games in a few simple steps. Many of the plugins are maintained by the Defold Foundation, but there are also plenty of examples of popular community created plugins. The extension system has without a doubt been a large contributing factor to the continued adoption and use of Defold among game developers!

One problem with the extension system is the development and operation of the build servers themselves. Up until now the build servers have been large monolithic servers with unwieldy setup scripts, running on [Amazon Web Services](https://aws.amazon.com/) (AWS). This setup has been a source of frustration for the development team and it has without a doubt prevented many developers from contributing improvements to the build servers and from setting up their own local or cloud hosted servers. Another concern is that the build servers are provided for free to all of our users and as our userbase has grown year over year we've also seen our AWS costs increase significantly. The servers are running 24/7 which means a fixed cost for the servers, but network traffic and storage costs have gone up, and there's been a general price increase for the servers themselves.

A couple of months ago we made the decision to try and improve the situation by simplifying the setup and operation while at the same time trying to reduce costs. We are now happy to announce that we've finished a large overhaul of the build servers. The servers are now split up into multiple instances where each instance is serving builds for a single platform. This will give us flexibility to quickly scale servers up and down depending on use, and even suspend servers that are inactive for a period of time.

The servers have also been migrated from AWS to [Google Cloud Platform](https://cloud.google.com/) (GCP) and the containers for each platform are available from a public container registry on GCP. The public container registry greatly simplifies the work involved in setting up your own local build servers or servers running on your own GCP account.

Finally, we have also started using [Terraform](https://www.terraform.io/) to describe the cloud builder infrastructure as code, which makes it easier to track and deploy changes.

The new system has been running for a month and we are very happy with the results. The setup is easier to maintain and operate and it will help us save money. It is now also a lot easier for users to set up their own build servers in a few easy steps. Have a look at the instructions below and try it out yourself!


## Setting up local cloud builders

Before you can run a local cloud builder you need to install the following software:

* [Docker](https://www.docker.com/) - Docker is a set of platform as a service products that use OS-level virtualization to deliver software in packages called containers. To run the cloud builders on your local development machine you need to install [Docker Desktop](https://www.docker.com/products/docker-desktop/)
* Google Cloud CLI - The Google Cloud CLI is a set of tools to create and manage Google Cloud resources. The tools can be [installed directly from Google](https://cloud.google.com/sdk/docs/install) or from a package manager such as Brew, Chocolatey or Snap.

You also need a Google account to download the containers with the platform specific build servers.

Once you have the above mentioned software installed follow these steps to install and run the Defold cloud builders:

- 1. Authorize to Google Cloud and create Application default credentials:

```sh
gcloud auth application-default login
```

- 2. Configure Docker to use Artifact registries:

```sh
gcloud auth configure-docker europe-west1-docker.pkg.dev
```

- 3. Check that everything set up correctly by pulling base image (make sure Docker Desktop is running!):

```sh
docker pull --platform linux/amd64 europe-west1-docker.pkg.dev/extender-426409/extender-public-registry/extender-base-env:latest
```

- 4. Clone `Extender` repository and switch to cloned repository root folder:

```sh
git clone https://github.com/defold/extender.git
cd extender
```

- 5. Download prebuilt jars:


```sh
TMP_DIR=$(pwd)/server/_tmp
APPLICATION_DIR=$(pwd)/server/app

# set nesessary version of Extender and Manifest merge tool
# versions can be found at Github release page https://github.com/defold/extender/releases
# or you can pull latest version like in this example

# get latest extender version
EXTENDER_VERSION=$(gcloud artifacts versions list \
	--location=europe-west1 \
	--repository=extender-maven \
	--package="com.defold.extender:server" \
	--sort-by="~createTime" \
	--limit=1 \
	--format="get(name)" | awk -F'/' '{print $NF}')

# get latest manifest merge tool version
MANIFESTMERGETOOL_VERSION=$(gcloud artifacts versions list \
	--location=europe-west1 \
	--repository=extender-maven \
	--package="com.defold.extender:manifestmergetool" \
	--sort-by="~createTime" \
	--limit=1 \
	--format="get(name)" | awk -F'/' '{print $NF}')

echo "Download prebuild jars to ${APPLICATION_DIR}"
rm -rf ${TMP_DIR}
mkdir -p ${TMP_DIR}
rm -rf ${APPLICATION_DIR}
mkdir -p ${APPLICATION_DIR}

gcloud artifacts files download \
	--project=extender-426409 \
	--location=europe-west1 \
	--repository=extender-maven \
	--destination=${TMP_DIR} \
	com/defold/extender/server/${EXTENDER_VERSION}/server-${EXTENDER_VERSION}.jar

gcloud artifacts files download \
	--project=extender-426409 \
	--location=europe-west1 \
	--repository=extender-maven \
	--destination=${TMP_DIR} \
	com/defold/extender/manifestmergetool/${MANIFESTMERGETOOL_VERSION}/manifestmergetool-${MANIFESTMERGETOOL_VERSION}.jar

cp ${TMP_DIR}/$(ls ${TMP_DIR} | grep server-${EXTENDER_VERSION}.jar) ${APPLICATION_DIR}/extender.jar
cp ${TMP_DIR}/$(ls ${TMP_DIR} | grep manifestmergetool-${MANIFESTMERGETOOL_VERSION}.jar) ${APPLICATION_DIR}/manifestmergetool.jar
```

- 6. Run docker compose main command to start the server:

```sh
docker compose -p extender -f server/docker/docker-compose.yml --profile <profile> up
```

where `profile` can be:

* __all__ - runs remote instances for every platform
* __android__ - runs remote instances to build Android version
* __web__ - runs remote instances to build Web version
* __linux__ - runs remote instances to build Linux version
* __windows__ - runs remote instances to build Windows version
* __metrics__ - runs VictoriaMetrics + Grafana as metrics backend and tool for visualization

Several profiles can be passed to the command line. The following example runs Android, Web and Windows instances:

```sh
docker compose -p extender -f server/docker/docker-compose.yml --profile android --profile web --profile windows up
```

For more information about docker compose arguments see https://docs.docker.com/reference/cli/docker/compose/. When docker compose is up you can use http://localhost:9000 as Build server address in the Editor's preference or as `--build-server` value if you use Bob to build the project.

To stop services press Ctrl+C if docker compose runs in non-detached mode, or if docker compose was run in detached mode (e.g. '-d' flag was passed to docker compose up command):

```sh
docker compose -p extender down
```


## Getting help and reporting problems

The system has been up and running for a while now but if you encounter any problems or have discovered a bug, please report them in the [build server repository](https://github.com/defold/extender) or reach out on the [Defold forum](https://forum.defold.com/).