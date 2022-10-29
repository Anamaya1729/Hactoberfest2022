function subArray(arr, start, end){
 
  let subArr=arr.slice(start, end)
  
  return subArr;
}
console.log(subArray([1, 2, 3, 4, 5], 1, 3))
