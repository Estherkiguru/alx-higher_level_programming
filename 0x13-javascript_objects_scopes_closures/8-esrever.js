#!/usr/bin/node

exports.esrever = function (list) {
  return list.reduceRight((acc, current) => {
    acc.push(current);
    return acc;
  }, []);
};
