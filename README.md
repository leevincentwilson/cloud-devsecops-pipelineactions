# Cloud DevSecOps Composite actions repository
![Public repository attention](https://img.icons8.com/ios/32/000000/error--v1.png)
**Please note** this repository is **Public** and as such no sensitive data should be stored. 

## Summary :
This repository is used to store reusable composite actions that other product teams can use to enhance their github actions pipeline.


#### List of Actions and parameters available to call the actions


### CI maven Build and Package Push:

#### call:  DigitalInnovation/cloud-devsecops-pipelineactions/workflows/CI@latest

##### inputs:
- **build_tool: maven**  -- Required		`{` *build tools you are using, we support maven and gradle more tools will be added* `}`
- **build_file_path: .** 				 `{` *path to the pom file default = .* `}`
- **build_file_name: pom.xml** `{` *Pom file name , default = pom.xml* `}`
- **settings_file_path: .** 	`{` *maven settings file path if you need push package, default *. `}`
- **settings_file_name: settings.xml** 	`{` *maven settings file name if you need push package, default settings.xml* `}`
- **build_phases: clean deploy**  `{` *stages to run as part of the build* `}`
- **build_arguments: -Dkey1=value1 -Dkey2=value2**  `{` *additional maven arguments to be passed for the build execution* `}`
- **az_artifact_repository_pat: ${{secrets.AZURE_ARTIFACT_PAT}}** 	`{` *you repository token to use for connecting to Azure package repository* if not already in setting.xml`}`
- **run_code_analysis:: true/false**  `{` *Flag to run Code Quality Scan* `}`
- **cq_project_key: CMTEST**  `{` *codeQulaity project key* `}`
- **cq_host_url: clean deploy**  `{` *Url of the Code Scanner Destination* `}`
- **cq_token: clean deploy**  `{` *Token to authenticate to the Project `}`

</br>
</br>

### Push Image built to ACR

#### call: DigitalInnovation/cloud-devsecops-pipelineactions/workflows/push\_image@latest

##### inputs:
- **cr_imagename: 'nginx'**  					`{` *docker image name* `}`
- **cr_imagetag: ${{ github.run\_id }}** 		`{` *docker image tag* `}`
- **cr_username: ${{ secrets.ACR\_USER }}** 		`{` *container registry user* `}`
- **cr_password: ${{ secrets.ACR\_PASS }}** 		`{` *container registry password* `}`
- **cr_servername: ${{ secrets.ACR\_SERVER }}** 	`{` *container registry servername* `}`
- **cr_dockerfile_name: Dockerfile** 	`{` *dockerfile name* `}`
- **cr_dockerfile_path: ci-helper/** 	`{` *relative path of the docker file* `}`
- **cr_subscription: ${{ secrets.ACR\_subscription }}** 	`{` *container registry subscription* `}`  
- **cr_tenant: ${{ secrets.ACR\_tenant }}** 	`{` *container registry tenant* `}`  

</br>
</br>

### Run Application Security Scan.
#### call: DigitalInnovation/cloud-devsecops-pipelineactions/workflows/appsec@latest

##### Parameters for Dependency (SNYK) Scan

- **run_dependency_scan: true/false** 	`{` *flag to execute dependency scan* `}`
- **dependency_scan_token: ${{ secrets.SNYK\_TOKEN }}** 	`{` *snyk token * `}`
- **dependency_scan_arguments: -Dkey=value** 	`{` *snyk maven arguments to pass* `}`

##### parameters for SAST (Fortify) Scan

- **run_sast_scan: true/false** 	`{` *flag to execute sast scan* `}`
- **sast_release_id: ${{ secrets.FOD\_RELEASE\_ID }}** 	`{` *your FOD project Release ID* `}`
- **sast_api_key: ${{ secrets.FOD\_API\_KEY}}** 			`{` *FOD key* `}`
- **sast_api_secret: ${{ secrets.FOD\_API\_SECRET}}** 	`{` *FOS secret* `}`
- **project_name: sample**  							`{` *name of the project ( used to great the zip file)* `}`
- **project_src_path: ./src** 						`{` *location of source to Zip for FOS push* `}`

##### Parameters for Container(Prisma) Scan

- **run_container_scan: true/false** 	`{` *flag to execute container scan* `}`
- **container_scan_user: ${{ secrets.username}}** 			`{` *container scan url user* `}`
- **container_scan_password: ${{ secrets.password}}** 	`{` *container scan url password* `}`
- **container_scan_url: sample**  							`{` *url of the container scan tool* `}`
- **docker_image_name: ./src** 						`{` *docker image name to scan* `}`
- **docker_image_tag: ./src** 						`{` *docker image tag to scan* `}`

</br>

