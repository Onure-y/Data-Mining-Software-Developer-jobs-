class DataModel:
    def __init__(self):
        self.allJobs = []

    def addNewJobToAllJobs(self, job_name, comp_name, job_location, job_type, job_add_date):
        job = {}
        job['jobName'] = ' '.join(job_name.split('\n')[1].split())
        job['compName'] = ' '.join(comp_name.split('\n')[1].split())
        job['jobLocation'] = ' '.join(job_location.split('\n')[1].split())
        job['jobType'] = job_type
        job['jobAddDate'] = job_add_date
        self.allJobs.append(job)

    def getLength(self):
        print(len(self.allJobs))

    def printAllData(self):
        for job in self.allJobs:
            print(job)


