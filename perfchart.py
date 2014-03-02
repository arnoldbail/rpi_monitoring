#!/usr/bin/env python

import cgi
import cgitb

# enable tracebacks of exceptions
cgitb.enable()

# print data from a file formatted as a javascript array
# return a string containing the table
# 
def print_table(filename,delimiter):
    data_lines=[]
    data_lines1=[]
    result=""
    with open(filename) as data_file:
        data_lines1=data_file.readlines()
        log_timestamp= data_lines1[0][12:]
        del data_lines1[0]
        data_lines=sorted(data_lines1,reverse=True)
        for line in data_lines[:-1]:
            x, y=line.strip('\n').split(delimiter)
            result += "['"+x+"', "+y+"],\n"
        else:
            x, y=data_lines[-1].strip('\n').split(delimiter)
            result += "['"+x+"', "+y+"]"

    return result

# print an HTTP header
# 
def printHTTPheader():
    print "Content-type: text/html"
    print ""
    print ""


def main():

 printHTTPheader()

    # this string contains the web page that will be served
    page_str="""
    <h1>CSU Parallel Clusters Remote Monitoring</h1>

    <script type="text/javascript" src="https://www.google.com/jsapi">
</script>
    <script type="text/javascript">
      google.load("visualization", "1", {packages:["corechart"]});
      google.setOnLoadCallback(drawChart);
      function drawChart() {
        var data = google.visualization.arrayToDataTable([
    ['Processor', 'secs'],
    %s
        ]);

        var options = {
          title: 'Real-time Processors Performance',
          hAxis: {title: 'Processors', titleTextStyle: {color: 'blue'}},
          vAxis: {title: 'Seconds', titleTextStyle: {color: 'blue'}}
        };

        var chart = new google.visualization.ColumnChart
                (document.getElementById('chart_div'));
        chart.draw(data, options);
      }
    </script>
    <div id="chart_div"></div>

    </body>
    """ % print_table('/var/www/rpimon.log', ';')

    # serve the page with the data table embedded in it
    print page_str



if __name__=="__main__":
    main()


