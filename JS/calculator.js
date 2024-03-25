function add(x, y) {
    return x + y;
  }
  
  function subtract(x, y) {
    return x - y;
  }
  
  function multiply(x, y) {
    return x * y;
  }
  
  function divide(x, y) {
    if (y === 0) {
      return "Error: Division by zero!";
    }
    return x / y;
  }
  
  function calculator() {
    console.log("Welcome to the Functional Calculator!");
    console.log("Select operation:");
    console.log("1. Add");
    console.log("2. Subtract");
    console.log("3. Multiply");
    console.log("4. Divide");
  
    const choice = prompt("Enter choice (1/2/3/4): ");
  
    if (!['1', '2', '3', '4'].includes(choice)) {
      console.log("Invalid choice!");
      return;
    }
  
    const num1 = parseFloat(prompt("Enter first number: "));
    const num2 = parseFloat(prompt("Enter second number: "));
  
    switch (choice) {
      case '1':
        console.log("Result:", add(num1, num2));
        break;
      case '2':
        console.log("Result:", subtract(num1, num2));
        break;
      case '3':
        console.log("Result:", multiply(num1, num2));
        break;
      case '4':
        console.log("Result:", divide(num1, num2));
        break;
      default:
        console.log("Invalid choice!");
    }
  }
  
  calculator();
  