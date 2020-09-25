def get_status_string(status_code):
    status_code = int(status_code) #convert just in case
    # """ 1xx # """
    if status_code == 100:
        return "Continue"
    elif status_code == 101:
        return "Switching Protocols"
    elif status_code == 102:
        return "Processing"
    elif status_code == 103:
        return "Early Hints"
    # """ 2xx # """
    elif status_code == 200:
        return "OK"
    elif status_code == 201:
        return "Created"
    elif status_code == 202:
        return "Accepted"
    elif status_code == 203:
        return "Non-Authoritative Information"
    elif status_code == 204:
        return "No Content"
    elif status_code == 205:
        return "Reset Content"
    elif status_code == 206:
        return "Partial Content"
    elif status_code == 207:
        return "Multi-Status"
    elif status_code == 208:
        return "Already Reported"
    elif status_code == 226:
        return "IM Used"
    # """ 3xx # """
    elif status_code == 300:
        return "Multiple Choices"
    elif status_code == 301:
        return "Moved Permanently"
    elif status_code == 302:
        return "Found"
    elif status_code == 303:
        return "See Other"
    elif status_code == 304:
        return "Not Modelified"
    elif status_code == 305:
        return "Use Proxy"
    elif status_code == 306:
        return "Switch Proxy"
    elif status_code == 307:
        return "Temporary Redirect"
    elif status_code == 308:
        return "Permanent Redirect"
    # """ 4xx # """
    elif status_code == 400:
        return "Bad Request"
    elif status_code == 401:
        return "Unauthorised"
    elif status_code == 402:
        return "Payment Required"
    elif status_code == 403:
        return "Forbidden"
    elif status_code == 404:
        return "Not Found"
    elif status_code == 405:
        return "Method Not Allowed"
    elif status_code == 406:
        return "Not Acceptable"
    elif status_code == 407:
        return "Proxy Authentication Required"
    elif status_code == 408:
        return "Request Timeout"
    elif status_code == 409:
        return "Conflict"
    elif status_code == 410:
        return "Gone"
    elif status_code == 411:
        return "Length Required"
    elif status_code == 412:
        return "Precondition Failed"
    elif status_code == 413:
        return "Payload Too Large"
    elif status_code == 414:
        return "URI Too Long"
    elif status_code == 415:
        return "Unsupported Media Type"
    elif status_code == 416:
        return "Range Not Satisfiable"
    elif status_code == 417:
        return "Exception Failed"
    elif status_code == 418:
        return "I'm A Teapot"
    elif status_code == 421:
        return "Misdirected Request"
    elif status_code == 422:
        return "Unprocessable Entity"
    elif status_code == 423:
        return "Locked"
    elif status_code == 424:
        return "Failed Dependency"
    elif status_code == 425:
        return "Too Early"
    elif status_code == 426:
        return "Upgrade Required"
    elif status_code == 428:
        return "Precondition Required"
    elif status_code == 429:
        return "Too Many Requests"
    elif status_code == 431:
        return "Request Header Fields Too Large"
    elif status_code == 451:
        return "Unavailable For Legal Reasons"
    # """ 5xx # """
    elif status_code == 500:
        return "Internal Server Error"
    elif status_code == 501:
        return "Not Implemented"
    elif status_code == 502:
        return "Bad Gateway"
    elif status_code == 503:
        return "Service Unavailable"
    elif status_code == 504:
        return "Gateway Timeout"
    elif status_code == 505:
        return "HTTP Version Not Supported"
    elif status_code == 506:
        return "Variant Also Negotiates"
    elif status_code == 507:
        return "Insufficient Storage"
    elif status_code == 508:
        return "Loop Detected"
    elif status_code == 510:
        return "Not Extended"
    elif status_code == 511:
        return "Network Authentication Required"
    # """ Unofficial Codes # """
    elif status_code == 218:
        return "This Is Fine"
    elif status_code == 419:
        return "Page Expired"
    elif status_code == 420:
        return "Method Failure | Enhance Your Calm"
    elif status_code == 430:
        return "Request Header Fields Too Large"
    elif status_code == 450:
        return "Blocked By Windows Parental Controls"
    elif status_code == 498:
        return "Invalid Token"
    elif status_code == 499:
        return "Token Required"
    elif status_code == 509:
        return "Bandwidth Limit Exceeded"
    elif status_code == 526:
        return "Invalid SSL Certelificate"
    elif status_code == 529:
        return "Site Is Overloaded"
    elif status_code == 530:
        return "Site Is Frozen"
    elif status_code == 598:
        return "Network Read Timeout Error"
    # """ Microsoft IIS # """
    elif status_code == 440:
        return "Login Time-Out"
    elif status_code == 449:
        return "Retry With"
    elif status_code == 451:
        return "Redirect"
    # """ nginx # """
    elif status_code == 444:
        return "No Response"
    elif status_code == 494:
        return "Request Header Too Large"
    elif status_code == 495:
        return "SSL Certelificate Error"
    elif status_code == 496:
        return "SSL Certelificate Requred"
    elif status_code == 497:
        return "HTTP Request Sent To HTTPS Port"
    elif status_code == 499:
        return "Client Closed Request"
    # """ Cloudflare # """
    elif status_code == 520:
        return "Web Server Returned An Unknown Error"
    elif status_code == 521:
        return "Web Server Is Down"
    elif status_code == 522:
        return "Connection Timed Out"
    elif status_code == 523:
        return "Origin Is Unreachable"
    elif status_code == 524:
        return "A Timeout Occurred"
    elif status_code == 525:
        return "SSL Handshake Failed"
    elif status_code == 526:
        return "Invalid SSL Certelificate"
    elif status_code == 527:
        return "Railgun Error"
    elif status_code == 530:
        return "This Error IS Accompanied With A 1XXX Error. Search For The Specelific 1XXX Error Within The Cloudflare Help Centre For More Information"
    # """ AWS Load Balancer # """
    elif status_code == 460:
        return "Client Closed Connection Before Idle Timeout Period Elapsed"
    elif status_code == 463:
        return "Load Balancer Received An X-Forwarded-For Request Header With More Than 30 IP Addresses"
    # """ Unknown # """
    else:
        return "Status Code Is Not Implemented Or Unknown"
    

















    