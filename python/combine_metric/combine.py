import json
import pandas as pd
import pyarrow.parquet as pq
import pyarrow as pa

def append_to_parquet_table(from_file=None, to_file=None, writer=None):

    with open(from_file,'r') as f:
        a = json.load(f)

    # add checkers here: possibly redo the
    # query depending on the results
    stat = a["status"]
    print("status: {}".format(stat))
    assert(stat == "success")

    d = a["data"]
    result_type = d["resultType"]
    print("resultType: {}".format(result_type))
    assert(result_type == "matrix")

    # convert the data into a pd.DataFrame

    # a currying helper
    def update_dict_0(adict):
        def update_dict(x):
            adict.update({"time": x[0], "value": x[1]})
            return adict
        return update_dict

    # result is list of dictionaries (json objects),
    # each of which has a metric and various values
    # associated with each metric:
    #
    # result: [{"metric":{}, "values": []},
    #          {"metric":{}, "values": []}]
    #
    # the list of values consists of [time, value]
    # elements.
    #
    # we would like to break each value into
    # {"time": time, "value": value} dictionaries
    #
    # and merge this dictionary with the associated
    # metric dictionary
    #
    # {"__name__": nameA, "instance": instanceA, "time": time0, "value": value0}
    # {"__name__": nameA, "instance": instanceA, "time": time1, "value": value1}
    # ...
    #
    # this is effectively an outer product of the metric with the value 2-tuple
    # single metric {<a>...<f>} values [[A],[B],...] become a list
    # [{<a>..<f>,< :A[0]>< :A[1]>},
    #  {<a>..<f>,< :B[0]>< :B[1]>}, ...]
    #
    # all metrics are then 'reduced' into a single list

    asum = []
    for k in d["result"]:
        adict = k["metric"]
        afun = update_dict_0(adict)
        tv = list(map(afun, k["values"]))
        asum += tv

    # save into a parquet file
    df = pd.DataFrame(asum)
    table = pa.Table.from_pandas(df)
    if writer is None:
        writer = pq.ParquetWriter(to_file, table.schema)
    writer.write_table(table=table)
    return (writer, df)

def read_parquet(from_file=None):
    # reading from parquet
    table = pq.read_table(from_file)
    df = table.to_pandas()
    return df

def test_append_to_parquet_table():
    writer = None
    writer, df = append_to_parquet_table(
        from_file="1537774538",
        to_file="example.parquet",
        writer=writer)
    writer.close()
    df2 = read_parquet(from_file="example.parquet")
    assert(df2.equals(df))

def test_append_to_parquet_table2():
    # test on multiple files
    timestamps = [1537774538, 1537775124, 1537775128, 1537775115, 1537775125,
                  1537775129, 1537775119, 1537775126, 1537775130, 1537775123,
                  1537775127, 1537776276]

    # write
    dfs = []
    writer = None
    for from_file in timestamps:
        writer, df = append_to_parquet_table(
            from_file=str(from_file),
            to_file="example.parquet",
            writer=writer)
        print(df.shape)
        dfs.append(df)
    writer.close()

    df = dfs[0]
    for d in dfs[1:]:
        df = df.append(d)
        print(df.shape)
    print(df.shape)

    # read
    df2 = read_parquet(from_file="example.parquet")
    print(df2.shape)

    assert(df2.equals(df))

if __name__=="__main__":
    test_append_to_parquet_table2()
