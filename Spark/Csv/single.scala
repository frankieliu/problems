** with coalesce
val ds = List((1,"one"),(2,"two")).toDF("num","str")
ds.coalesce(1).
  write.
  mode("overwrite").
  option("header","true").
  option("delimiter",",").
  csv(filename)

val path=dbutils.fs.ls(filename+"/").
  filter(f => f.name.endsWith(".csv"))(0).path

dbutils.fs.cp(path,filename+".csv")
dbutils.fs.rm(filename+"/", recurse=true)

** writing without without coalesce
If you are running Spark with HDFS, I've been solving the problem by writing csv files normally and leveraging HDFS to do the merging. I'm doing that in Spark (1.6) directly:

import org.apache.hadoop.conf.Configuration
import org.apache.hadoop.fs._

def merge(srcPath: String, dstPath: String): Unit =  {
   val hadoopConfig = new Configuration()
   val hdfs = FileSystem.get(hadoopConfig)
   FileUtil.copyMerge(hdfs, new Path(srcPath), hdfs, new Path(dstPath), true, hadoopConfig, null)
   // the "true" setting deletes the source files once they are merged into the new output
}


val newData = << create your dataframe >>


val outputfile = "/user/feeds/project/outputs/subject"
var filename = "myinsights"
var outputFileName = outputfile + "/temp_" + filename
var mergedFileName = outputfile + "/merged_" + filename
var mergeFindGlob  = outputFileName

    newData.write
        .format("com.databricks.spark.csv")
        .option("header", "false")
        .mode("overwrite")
        .save(outputFileName)
    merge(mergeFindGlob, mergedFileName )
    newData.unpersist()
