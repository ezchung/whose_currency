"use strict";

/** Check if two string are at most a single edit away from being identical
 * Input: Two strings       Output: boolean of whether they are almost identical
 */
function almostIdentical(word1, word2) {
  let word1Len = word1.length;
  let word2Len = word2.length;
  if (Math.abs(word1Len - word2Len) > 1) return false;

  let wordOrder = categorizeWordsByLen(word1, word2);

  let longPoint = 0;
  let shortPoint = 0;
  let chance = 1;
  if (word1Len === word2Len) {
    for (let i = 0; i < word1Len; i++) {
      if (word1[longPoint] != word2[shortPoint]) {
        longPoint++;
        shortPoint++;
        if (chance <= 0) return false;
        chance--;
      } else if (word1[longPoint] === word2[shortPoint]) {
        longPoint++;
        shortPoint++;
      }
    }
  } else {
    for (let i = 0; i < wordOrder[0].length; i++) {
      if (wordOrder[0][longPoint] != wordOrder[1][shortPoint]) {
        longPoint++;
        if (chance <= 0) return false;
        chance--;
      } else if (wordOrder[0][longPoint] === wordOrder[1][shortPoint]) {
        longPoint++;
        shortPoint++;
      }
    }
  }
  return true;
}

/** Input: Two strings. Output: array
 * Recieve two strings and return an array organized by length, ascending order
 */

function categorizeWordsByLen(word1, word2) {
  if (word1.length >= word2.length) {
    return [word1, word2];
  } else return [word2, word1];
}

//Problem
//check if two words are almost identical, meaning at most there is a one letter
//difference
//Input: two str        Output: Boolean

//Examples
//(make,fake) => true
//(task,take) => false
//(asks, ask) => true
//(asking, ask) => false
//(tile, liter) => false

//PseudoCode
//Fast fail
//if length of word1 - length of word2 is greater than 1, then return false

//check that the two are within one length from each other
//find the longest word
//if string lengths are equal to each other
//use this method
//two pointers and if the char at index pointers are equal, increment both
//pointers. If not, then increase both and decrease chances by one after checking
//if chances greater than zero
//If string lengths are not equal
//use this method
//two pointers. if chars are index pointers are not equal, increase the
//long pointer. check if chance is greater than 0, if it is, decrease by one
//if chars are equal, increase both pointers
