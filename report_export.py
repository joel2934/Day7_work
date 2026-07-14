import csv

def export_vehicle_data(filename , vehicles):
    with open(filename , 'w',newline='') as file:
        writer=csv.writer(file)
        writer.writerow(['Brand','Model','Year','Owner'])
        #writer.writerow([vehicle.brand , vehicle.model , vehicle.year , vehicle.owner])

        for v in vehicles:
            owner =v.get_owner()
            if owner is None:
                owner = "No owner assigned"
            else:
                owner=owner.replace("Owner: ","").strip()

            #battery_capacity = getattr(v,'battery_capacity',None)
            writer.writerow([v.brand , v.model,v.year , owner])
    return f"Vehicle data exported to {filename} successfully"