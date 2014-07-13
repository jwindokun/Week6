#
# URL of website: http://money.cnn.com/pf/features/lists/nar_1q05/price.html
require(XML)
library(XML)
theurl = "http://money.cnn.com/pf/features/lists/nar_1q05/price.html"
myData = readHTMLTable(theurl, header = TRUE,
                       colClasses = NULL, skip.rows = c(141,142), trim = TRUE,
                       elFun = xmlValue, as.data.frame = TRUE, which = 5)
myData

