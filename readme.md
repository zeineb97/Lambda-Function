# Subject : Virtualisation Cloud


> This project is an academic project developed within the framework of validation of the comprehension of the Lambda Functions throw implementing a cloud Lambda Funtion.

[INSAT](http://www.insat.rnu.tn) with the option: DevOps and software testing.
---

> S3 Thumbnail Creator - Developed by Zeineb Chabchoub

### Table of contents
- [Overview](#overview)
- [Workflow](#workflow)
- [Steps](#steps)


## Overview
We will create an S3 bucket that contains 2 different directories, in one directory, we are able to upload images, huge  ones. When an image is uploaded, a Lambda Function must be triggered to resize this image and stored in the other directory. 

#### Workflow 

![Workflow Image](https://gccontent.blob.core.windows.net/gccontent/blogs/gcdocuments/20190121-create-a-thumbnail-image-using-documents-for-imaging/image3.png)


## Steps

- Create S3 Bucket.
- Create 2 different directories within the bucket.
- Go to AWS Lambda --> Functions.
- Build your function ( I choose to build it with a python runtime Language).
- Add Trigger to the created Lambda Function :  (our trigger is S3 --> choose your created Bucket  --> Event : All object create events)
