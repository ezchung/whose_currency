function scrambledPalindromeCheck(word) {
  let wordLen = word.length;

  if (wordLen <= 1) return true;

  let letter_group = [];

  for (let char of word) {
    if (letter_group.includes(char)) {
      let letter_position = letter_group.indexOf(char);
      letter_group.splice(letter_position, 1);
    } else {
      letter_group.push(char);
    }
  }

  if (wordLen % 2 === 0 && letter_group.length === 0) {
    return true;
  } else if (wordLen % 2 === 1 && letter_group.length === 1) {
    return true;
  }
  return false;
}

//Problem
//Take a word and return boolean if the letters provided while reconfiguing
//ever brind a word that is a palindrome
//Input: String of letters
//Output: Boolean

//Representation
// (carrace) => true (racecar)
// (e) => true
// (zzzaaa) => false
// (bba) => true

//Pseudo Code
//when can they be a palindrome

//if word is even count. Everyone should have a pair
//if word is odd count. There should be one letter that doesnt have a pair
//if not then false

//create an array
//iterate through word
//if letter is in array
//remove letter from array
//if not,
//add letter to array
//if word length is even, list should be empty
//if odd, list should have a length of one
//or else return false
