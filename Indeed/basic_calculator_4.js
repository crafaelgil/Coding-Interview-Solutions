const basicCalculatorIV = function(expression, evalvars, evalints) {
  const record = {}; // { variable: value, ... }
  evalvars.forEach((k, i) => record[k] = evalints[i]);
  const expr = calculator(expression); // expr: { expr: coeff, ... }
  const terms = collectTerms(expr);
  const ans = buildOutput(expr, terms);
  return ans;

  // calculator will return the final expr like: { e*e: 1, #: 64 }
  function calculator(expression) {
    if (!expression.length) return {};

    expression += " +"; // this is to trigger adding `cur` to `result`,
                        // otherwise, it might stop when finish calculating `cur`.
    const n = expression.length;
    let result = {}, cur = {};
    let operator = "+", i;
    for (i = 0; i < n; i += 2) { // i += 2 because there's a space between each expression
      const expr = getExpr();    // recursively to get the nested expr
      // first try an expression with no parentheses and log the expr
      // then try an expression with parentheses and log the expr
      // You'll probably get a feel how the recursion works
      if (["+", "-", "*"].includes(expression[i]) || i == n - 1) {
        // update cur based on operators,
        // for example for expression "e + 8", cur will have values: { e: 1 } and { #: 8 }
        // result will have values: { e: 1 } and then { e: 1, #: 8 }.
        if (operator == "+") cur = add(cur, expr);
        if (operator == "-") cur = sub(cur, expr);
        if (operator == "*") cur = mul(cur, expr);
        // if meet '+' or '-', we add cur to result.
        // also this is why we added the " +" to expression
        // because otherwise, for example when the expression is "a * b * c", then
        // cur will have values: { a: 1 }, { a*b: 1 }, and { a*b*c: 1 }.
        // but result will not get populated.
        if (["+", "-"].includes(expression[i]) || i == n - 1) {
          result = add(result, cur);
          cur = {};
        }
        operator = expression[i];
      }
    }
    return result;

    // calculator will return an expr like: { a: 1} for non-nested problem,
    // and { a: 1, b: 1, #: 8 } for a nested problem
    function getExpr() {
      if (i >= n) return result;

      let expr = {}, start = i;
      if (expression[i] == "(") { // found a subproblem
        const stk = [];
        stk.push(i);
        i += 1;
        // find boundaries of the subproblem,
        // if reaches the end of expression or parentheses pair closed
        while (i < n && stk.length) {
          if (expression[i] == "(") stk.push(i);
          if (expression[i] == ")") stk.pop();
          i += 1;
        }
        // the subproblem could look like this first: ((a - b) * (b - c) + (c - a))
        // then look like: a - b => { a: 1, b: 1 }
        // then look like: b - c => { b: 1, c: -1 }
        // then look like: c - a => { c: 1, a: -1 }
        const sub = expression.slice(start + 1, i-1);
        // for each of the subproblems above, calculator knows how to caculate it on its own,
        // it won't reach this part again, because the subproblem does not have '(' anymore.
        expr = calculator(sub);
      } else if (isdigit(expression[i])) { // collect digits expr, like { #: 84 }
        while (i < n && isdigit(expression[i])) i += 1;
        const val = expression.slice(start, i);
        expr["#"] = +val;
      } else {
        // collect expression key, like { a: 1 },
        // also it could be a pre-defined variable, so it becomes a constant
        while (i < n && expression[i] != " ") i += 1;
        const key = expression.slice(start, i);
        if (key in record) { // found variable constant
          expr["#"] = record[key];
        } else { // found a expression key
          expr[key] = 1;
        }
      }
      i += 1;
      return expr;
    }
  }

  function collectTerms(tree) {
    const terms = [];
    for (const [key, val] of Object.entries(tree)) {
      if (val && key != "#") {
        // order depends on how many '*' the key has
        const order = key.split("").filter(c => c == "*").length;
        terms.push([key, order]);
      }
    }
    // sort by order desc and key asc
    terms.sort((a, b) => a[1] != b[1] ? b[1] - a[1] : a[0].localeCompare(b[0]))
    return terms.map(([key]) => key);
  }

  function buildOutput(tree, terms) {
    const ans = terms.map(term => tree[term] + "*" + term);
    const constant = tree["#"];
    if (constant) ans.push(constant.toString());
    return ans;
  }
};

function isdigit(char) {
  return char >= "0" && char <= "9";
}

function combineKey(s1, s2) {
  return s1.split("*").concat(s2.split("*")).sort().join("*");
}

function add(a, b) {
  Object.entries(b).forEach(([k, v]) => a[k] = (a[k] || 0) + v);
  return a;
}

function sub(a, b) {
  Object.entries(b).forEach(([k, v]) => a[k] = (a[k] || 0) - v);
  return a;
}

function mul(a, b) {
  const ans = {};
  for (const [ak, av] of Object.entries(a)) {
    for (const [bk, bv] of Object.entries(b)) {
      if (ak == "#") {
        ans[bk] = (ans[bk] || 0) + av * bv;
      } else if (bk == "#") {
        ans[ak] = (ans[ak] || 0) + av * bv;
      } else {
        const key = combineKey(ak, bk);
        ans[key] = (ans[key] || 0) + av * bv;
      }
    }
  }
  return ans;
}
