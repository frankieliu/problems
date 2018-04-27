# copts = ["-Iexternal/googletest_git/googletest/include"],

cc_test(
    name = "leetcode_67_test",
    
    srcs = ["leetcode_67_test.cc",
            "leetcode_67.h"],
    
    deps = [
        "@usr_lib//:gtest_lib",
        "@gnu//:pthread_lib",
        "//base",
    ],
    
)

cc_binary(
    name = "run_leetcode_67_test",
    srcs = ["leetcode_67_test.cc",
            "leetcode_67.h"],
    deps = [
        "@usr_lib//:gtest_lib",
        "@gnu//:pthread_lib",
        "//base",
    ],
)