from urllib.parse import unquote

from mkpipe.spark import JdbcExtractor


class SqlserverExtractor(JdbcExtractor, variant='sqlserver'):
    driver_name = 'sqlserver'
    driver_jdbc = 'com.microsoft.sqlserver.jdbc.SQLServerDriver'

    def build_jdbc_url(self):
        password = unquote(self.password)
        return (
            f'jdbc:{self.driver_name}://{self.host}:{self.port}'
            f';databaseName={self.database}'
            f';user={self.username}'
            f';password={password}'
            f';encrypt=false;trustServerCertificate=false'
        )
