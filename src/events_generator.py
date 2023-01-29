from src.events_repository import EventsRepository
from src.private_data_repository import PrivateDataRepository

class EventsGenerator:
    def generate(self):
        print('Generate new events list')
        v2_by_ids = {}
        for default_event_v2 in EventsRepository.default_events_v2:
            id = default_event_v2['id']
            emoji_number = default_event_v2['emoji_number']
            en = default_event_v2['en']
            ru = default_event_v2['ru']
            v2_by_ids[id] = ru

        excel_by_id = {}
        for default_event_excel in EventsRepository.default_events_excel:
            id = default_event_excel['id']
            emoji_number = default_event_excel['emoji_number']
            ru = default_event_excel['ru']
            en = default_event_excel['en']
            ru_tag = default_event_excel['ru_tag']
            en_tag = default_event_excel['en_tag']
            excel_by_id[id] = ru

        for user_event_from_db in PrivateDataRepository.user_events_from_db:
            count = user_event_from_db['count']
            title = user_event_from_db['title']

        print('Find events with same ids:')
        v2_repls_count = 0
        for key in v2_by_ids.keys():
            if (key not in excel_by_id):
                print('Excel has no:', key, '-', v2_by_ids[key])
                v2_repls_count += 1

        excecl_repls_count = 0
        for key in excel_by_id.keys():
            if (key not in v2_by_ids):
                print('Default has no:', key, '-', excel_by_id[key])
                excecl_repls_count += 1

        print(f'Repls counts, v2: {v2_repls_count} excel: {excecl_repls_count}')

        print('SUCCESS')