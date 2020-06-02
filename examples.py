from api_utils import *


# set url
fhir_synthetic_mass_url = 'https://syntheticmass.mitre.org/v1/fhir/'

#set your api key
api_key = 'your_key_goes_here'

# retrieve 10 Patients
mycall = base_request(fhir_synthetic_mass_url, 'Patient', api_key, '_count=10')

# save Patients to a file
saved_file = save_data(mycall, 'patients_example')

# save Patients IDs in a separate file
patientsids = get_resources_ids(mycall, 'patientsids_example')

# retrieve Patients IDs from file
subjects_references = get_related_resources('Patient', get_ids_from_file('patientsids_example.txt'))

# Example 1. Get all DiagnosticReports for 100 Patients
# https://syntheticmass.mitre.org/v1/fhir/DiagnosticReport?&subject:reference=Patient/6f7acde....

all_diagnistic_reports = base_request(
    fhir_synthetic_mass_url,
    'DiagnosticReport',
    api_key,
    subjects_references
)

# save all DiagnosticReports
save_diagnostic_reports = save_data(all_diagnistic_reports, 'diagnostic_reports_example')


# Example 2. Get all Observations for 100 Patients
all_observations = base_request(
    fhir_synthetic_mass_url,
    'Observation',
    api_key,
    subjects_references
)

# save all Observations
save_observations = save_data(all_observations, 'observations_example')
