from collections import defaultdict

def aggregate_trips(trips: list[dict]) -> list[dict]:
  # trips: [{'user_id': str, 'origin': str, 'destination': str, 'duration_hours': int}]
  user_hours = defaultdict(int)
  user_cites = defaultdict(set)
  result = []
  for trip in trips:
    user_hours[trip['user_id']] += trip['duration_hours']
    user_cites[trip['user_id']].add(trip['destination'])
  
  for k,v in user_hours.items():
    d = {}
    d['user_id'] = k
    d['total_hours'] = user_hours[k]
    d['unique_destinations'] = len(user_cites[k])
    result.append(d)
    result.sort(key=lambda x: x['user_id'])
  return result
   
   
     





  return
