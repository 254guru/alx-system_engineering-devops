# Postmortem: Web Stack Outage Incident
<img src="images/julia-joppien-XFUqd0u5U7w-unsplash.jpg" alt="broken computer">
## Issue Summary

### Duration
Start Time: January 25, 2024, 10:30 AM (UTC)
End Time: January 25, 2024, 12:45 PM (UTC)

### Impact:
The outage affected the availability of our main web application, resulting in a 20% degradation of service for all users during the incident.

### Root Cause:
The root cause of the outage was identified as an unexpected spike in database connections, causing the database server to become unresponsive.

### Timeline
<li><strong>10:30 AM:</strong>Issue detected through automated monitoring alert indicating high response time and increased error rates.</li>
<li><strong>10:35 AM:</strong>Engaged the on-call engineer to investigate the issue. Initial assumption was a possible network latency problem.</li>
<li><strong>10:50 AM:</strong>Network latency ruled out. Investigation shifted to application layer. Checked application logs for errors.</li>
<li><strong>11:15 AM:</strong>Discovered an abnormal increase in database connection attempts. Assumed a possible DDoS attack and initiated DDoS mitigation procedures.</li>
<li><strong>11:45 AM:</strong>DDoS mitigation efforts did not improve the situation. Realized the issue was with the application code causing a surge in database connections.</li>
<li><strong>12:00 PM:</strong>Incident escalated to the Database and Application teams for further investigation and resolution.</li>
<li><strong>12:15 PM:</strong>Identified a code deployment that inadvertently introduced a database connection leak. Rolled back the deployment to a stable version.</li>
<li><strong>12:30 PM:</strong><img src="images/icons8-confetti.svg" alt="congrats">Database connections stabilized, and application performance improved. System returned to normal operation.</li>
<li><strong>12:45 PM:</strong>Incident officially declared resolved. Post-incident analysis meeting scheduled.</li>

## Root Cause and Resolution

### Root Cause:
The root cause was traced back to a recent code deployment that introduced a database connection leak. The leak resulted in an excessive number of open connections to the database server, eventually causing it to become unresponsive.

### Resolution:
The immediate resolution involved rolling back the problematic code deployment to a previously stable version. This action closed the database connections, restoring normal system behavior. Further, a code review process was implemented to prevent similar issues in the future.

## Corrective and Preventative Measures

### Improvements/Fixes:
<ol><li>Implement additional automated tests in the continuous integration pipeline to catch database connection issues during the pre-deployment phase.</li>
<li>Enhance monitoring capabilities to provide early detection of abnormal database connection patterns.</li></ol>

### Tasks:
<ol><li>Conduct a thorough review of the code deployment process, emphasizing the importance of code reviews and testing.</li>
<li>Implement stricter controls on database connection limits to prevent similar incidents.</li>
<li>Enhance documentation regarding the potential impact of code changes on database connections to raise awareness among developers.</li>
<li>Schedule a training session for the development team to increase awareness of best practices related to database connection management.</li></ol>

<p>This postmortem highlights the critical importance of robust monitoring, swift incident response, and a comprehensive review of deployment processes. By implementing these corrective and preventative measures, we aim to fortify our system against similar incidents in the future, ensuring a more resilient and reliable web stack.</p>
