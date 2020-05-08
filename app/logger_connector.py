import json
from app.article_logs import ArticleLogs
from app.log import Log


class LoggerConnector:
    def __init__(self, logger_file_name):
        self.logger_file_name = logger_file_name

    def read_json_file(self):
        with open(self.logger_file_name) as f:
            load = json.load(f)
        return load

    def get_all_logs(self):
        load = self.read_json_file()

        article_logs = list()
        logs = list()
        for i in load:
            obj = ArticleLogs(i['id'], i['logs'])
            for j in obj.logs:
                log = Log(j['id'], j['data'], j['text'])
                logs.append(log)
            article_logs.append(ArticleLogs(obj.id, logs))
            logs = []

        return article_logs

    def get_logs_by_id(self, id):
        load = self.read_json_file()
        #print(load)
        logs = list()
        article_logs = list()

        for i in load:
            obj = ArticleLogs(i['id'], i['logs'])
            if obj.id == id:
                for j in obj.logs:
                    log = Log(j['id'], j['data'], j['text'])
                    logs.append(log)
                article_logs.append(ArticleLogs(obj.id, logs))
                logs = []

        return article_logs

    def add_log(self, obj):
        articleLogs = self.get_all_logs()
        articleLogs.append(obj)

        with open(self.db_file_name, 'w') as f:
            json.dump([obj.__dict__ for obj in articleLogs], f)
