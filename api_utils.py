import requests
import json
import logging


logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler()
    ]
)


def base_request(url, resource_type, api_key, other_query_params=''):
    """ Connect to api, specify resource type and other query parameters and pass your registered api key. """

    # resource_type according to FHIR resources, be aware FHIR uses camelCase, case sensitive
    query_string = url + resource_type + '?'+ str(other_query_params) + '&apikey=' + api_key
    logging.info(f"Request: {query_string}")
    try:
        r = requests.get(query_string)
        data = r.json()
        logging.info(f"Total objects of resource type {resource_type.title()}: {len(data['entry'])}")
        return data
    except Exception as e:
        logging.error(f"Exception: {e}")


def save_data(data, output_name):
    """ Save the response to json file. """

    with open(f"{output_name}.json", "w", encoding="utf-8") as output_file:
        json.dump(data, output_file, ensure_ascii=False, indent=4)
    logging.info(f"The data is saved to {output_name}.json file.")
    return data


def get_resources_ids(data, output_name):
    """ Save all resources IDs to a file. """

    resources_ids = []
    with open(f"{output_name}.txt", "w") as output_file:
        for item in data["entry"]:
            obj_id = item["resource"]["id"]
            resources_ids.append(obj_id)
            output_file.write(obj_id + '\n')
    logging.info(f"IDs are saved to {output_name}.txt file.")
    output_file.close()
    return resources_ids


#  https://syntheticmass.mitre.org/v1/fhir/Condition?subject:reference=Patient/6f7acde5-db81-4361-82cf-886893a3280c&apikey=
def get_related_resources(resource_type, subject_ids: list):
    """ Returns a string that can be passed as a query parameter to retrieve all subject references. """

    subject_reference = 'subject:reference=' + resource_type.title() + '/'
    for subject in subject_ids:
        if subject != subject_ids[-1]:
            subject_reference += f"{subject},"
        else:
            subject_reference += subject
    logging.info(f"This is related subjects: {subject_reference}")
    return subject_reference


def get_ids_from_file(file_name):
    """ Get all resources IDs from the file. """

    with open(file_name, 'r') as f:
        ids = [line.strip() for line in f]
    return ids
