files={'Manifest':['ExportDataDictionary.csv','FileIntegrityManifest.csv','TableMetadata.csv'],
       'feature-table':['FeatureTable_feature_table'],
       'prose-aggregates':['Prose_age_at_index', 'Prose_census_region', 'Prose_closed_claims', 'Prose_ethnicity', 'Prose_race', 'Prose_sex', 'Prose_top25_ci', 'Prose_top25_dx', 'Prose_top25_px', 'Prose_top25_rx_req'],
       'thdm':['Account','AccountCoverage','AccountEncounter','AccountPaymentClassification','AllergyIntolerance','AllergyIntoleranceCodeConceptMap','AllergyIntoleranceCodeConceptMapHistory','AllergyIntoleranceManifestation','AntimicrobialSusceptibility','AntimicrobialSusceptibilityCodeConceptMap','AntimicrobialSusceptibilityCodeConceptMapHistory','BodySiteMap','BodySiteMapHistory','CareSite','CareSiteRequestHistory','CategoryConceptMap','CategoryConceptMapHistory','ChargeItem','ChargeItemCodeConceptMap','ChargeItemCodeConceptMapHistory','ClaimCode','ClaimLine','ClaimLineCodes','Concept','ConceptLink','Condition','ConditionCodeConceptMap','ConditionCodeConceptMapHistory','Coverage','DeviceUse','DeviceUseCodeConceptMap','DeviceUseCodeConceptMapHistory','Encounter','EncounterHistory','EncounterParticipant','Enrollment','EventLog','EventReference','Extract','ExtractSchema','FamilyMemberHistory','FamilyMemberHistoryCodeConceptMap','FamilyMemberHistoryCodeConceptMapHistory','FamilyMemberHistoryOutcomeConceptMap','FamilyMemberHistoryOutcomeConceptMapHistory','ImagingInstance','ImagingProperty','ImagingSeries','ImagingStudy','Immunization','ImmunizationCodeConceptMap','ImmunizationCodeConceptMapHistory','LabResult','LabResultCodeConceptMap','LabResultCodeConceptMapHistory','LabResultComponent','Location','MedicalClaim','MedicalClaimParticipant','MedicalClaimPaymentClassification','MedicationAdherenceReasonConceptMap','MedicationAdherenceReasonConceptMapHistory','MedicationAdministration','MedicationCodeConceptMap','MedicationCodeConceptMapHistory','MedicationDispense','MedicationRequest','MedicationStatement','Note','Observation','ObservationCodeConceptMap','ObservationCodeConceptMapHistory','ObservationComponent','Patient','Person','PersonDeathFact','PersonLocation','PersonRace','PersonTag','PharmacyClaim','Practitioner','PractitionerQualification','Procedure','ProcedureCodeConceptMap','ProcedureCodeConceptMapHistory','ServiceRequest','ServiceRequestCodeConceptMap','ServiceRequestCodeConceptMapHistory','Specimen','TemporalOrder']}


#need to print loop and preint all the files
raw_path='s3://test/data/csv/20260520/'
partial_dataset_dict={}
while True:
    for key, value in files.items():
        datasets=value
        # print(datasets)
        for dataset in datasets:
             if key=='Manifest':
                  dataset_name=dataset.replace('.csv','')
                  dataset_name='manifest_'+dataset_name
                  print(f'dest_dataset_name: {dataset_name}')
                  raw_file_path=raw_path+f'{key}/{dataset}'
                  print(raw_file_path)
             elif key=='feature-table':
                  dataset_name=dataset
                  print(f'dest_dataset_name: {dataset_name}')
                  raw_file_path=raw_path+f'{key}/{dataset}/*'
                  print(raw_file_path)
             elif key=='prose-aggregates':
                  dataset_name=dataset
                  print(f'dest_dataset_name: {dataset_name}')
                  raw_file_path=raw_path+f'{key}/{dataset}/*'
                  print(raw_file_path)
             else:
                   dataset_name='thdm_'+dataset
                   print(f'dest_dataset_name: {dataset_name}')
                   raw_file_path=raw_path+f'{key}/{dataset}/*'
                   print(raw_file_path)
             partial_dataset_dict = {
                    # "src_metadata_dataset_id": src_metadata_dataset_id,
                    "src_dataset_name" : dataset,
                    "raw_s3_file_path":raw_file_path,
                    # "dest_database_name": database_name,
                    # "dest_s3_key": f"{dest_database_name}.db/{dataset_name}/{version_timestamp_str}/",
                    # "dest_s3_key_with_out_version": f"{dest_database_name}.db/{dataset_name}/",
                    # "dest_s3_file_path": f"s3://{datalake_s3_bucket}/{dest_database_name}.db/{dataset_name}/{version_timestamp_str}/",
                    # "dest_s3_file_path_with_out_version": f"s3://{datalake_s3_bucket}/{dest_database_name}.db/{dataset_name}/",
                }

    break