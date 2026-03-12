#Import the necessary libraries
from google.cloud import iam_admin_v1
import argparse

#create a custom role with permissions to start and stop VM instances
def create_custom_role(project_id, role_id):
    client = iam_admin_v1.IAMClient()
    parent = f"projects/{project_id}"
    role = iam_admin_v1.Role(
        title= "VM Starter Stopper",
        included_permissions=[
            "compute.instances.start",
            "compute.instances.stop"
        ],
        stage=iam_admin_v1.Role.RoleLaunchStage.GA
    )
    request = iam_admin_v1.CreateRoleRequest(parent=parent,role_id=role_id,role=role)
    response = client.create_role(request=request)
    print(f"Created custom role: {response.name}")
#Example usage: python custom_role.py my-gcp-project myCustomRole

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a custom IAM role for starting and stopping VM instances.")
    parser.add_argument("project_id", help="The ID of the GCP project.")
    parser.add_argument("role_id", help="The ID for the custom role.")

    args = parser.parse_args()
#assign the project_id and role_id variables from the command line arguments
    create_custom_role(args.project_id, args.role_id)

#If you want to assign this custom role to a service account, you can use the following gcloud command:
#gcloud projects add-iam-policy-binding [PROJECT_ID] --member="serviceAccount:[SA_NAME]@[PROJECT_ID].iam.gserviceaccount.com" --role="projects/[PROJECT_ID]/roles/[ROLE_ID]"
#Every custom role created will have a unique identifier in the format: projects/[PROJECT_ID]/roles/[ROLE_ID], not like predefined roles which have a format like: roles/[ROLE_NAME]
