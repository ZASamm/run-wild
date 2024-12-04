/**
 * Credit to https://dev.to/codingcss/responsive-number-counting-animation-with-javascript-project-with-source-code-2m5
 * 
 * Initializes the number count-up animation for elements with the class "num".
 * The count-up animation starts from 0 and ends at the value specified in the "data-val" attribute.
 * The duration of the animation is distributed evenly based on the interval and the end value.
 */

document.addEventListener('DOMContentLoaded', () => {
  const valueDisplays = document.querySelectorAll(".num");
  const interval = 4000;

  valueDisplays.forEach(valueDisplay => {
      let startValue = 0;
      const endValue = parseInt(valueDisplay.getAttribute("data-val"), 10);

      if (isNaN(endValue)) {
          console.error("Invalid data-val attribute:", valueDisplay.getAttribute("data-val"));
          return;
      }

      const duration = Math.floor(interval / endValue);

      const counter = setInterval(() => {
          startValue += 1;
          valueDisplay.textContent = startValue;
          if (startValue === endValue) {
              clearInterval(counter);
          }
      }, duration);
  });
});