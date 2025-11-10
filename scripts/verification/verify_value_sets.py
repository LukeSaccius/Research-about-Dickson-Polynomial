"""
Verification Script for Dickson Polynomial Value Sets with Cardinality 2

This script verifies the theoretical proof by computing the actual value sets
for the three special indices that produce cardinality 2.

For prime p > 3:
- n₁ = p² - 1 should give value set {1, 2}
- n₂ = (p² + 1)/2 should give value set {1, p-1}
- n₃ = (p² + 2p - 1)/2 should give value set {1, p-1}
"""

def reversed_dickson_polynomial(n, x, p):
    """
    Compute the REVERSED Dickson polynomial D_n(1, x) mod p.
    
    This uses the recurrence relation from Test.py:
    D_0(1, x) = 2
    D_1(1, x) = 1
    D_n(1, x) = D_{n-1}(1, x) - x * D_{n-2}(1, x)
    """
    if n == 0:
        return 2 % p
    if n == 1:
        return 1 % p
    
    # Use iterative approach to avoid recursion depth issues
    d_prev = 2 % p  # D_0
    d_curr = 1 % p  # D_1
    
    for i in range(2, n + 1):
        d_next = (d_curr - x * d_prev) % p
        d_prev = d_curr
        d_curr = d_next
    
    return d_curr


def compute_value_set(n, p):
    """
    Compute the value set of D_n(1, x) for all x in F_p.
    Returns the set of all distinct outputs.
    """
    value_set = set()
    for x in range(p):
        value = reversed_dickson_polynomial(n, x, p)
        value_set.add(value)
    return value_set


def is_prime(num):
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def verify_for_prime(p):
    """
    Verify the three special cases for a given prime p > 3.
    """
    if p <= 3:
        print(f"Skipping p={p} (requires p > 3)")
        return
    
    print(f"\n{'='*60}")
    print(f"Prime p = {p}")
    print(f"{'='*60}")
    
    # Case 1: n = p² - 1, expected value set {1, 2}
    n1 = p**2 - 1
    vs1 = compute_value_set(n1, p)
    expected1 = {1, 2}
    match1 = vs1 == expected1
    print(f"\nCase 1: n = p² - 1 = {n1}")
    print(f"  Value set: {sorted(vs1)}")
    print(f"  Expected:  {sorted(expected1)}")
    print(f"  Match: {'✓' if match1 else '✗'}")
    
    # Case 2: n = (p² + 1)/2, expected value set {1, p-1}
    n2 = (p**2 + 1) // 2
    vs2 = compute_value_set(n2, p)
    expected2 = {1, p - 1}
    match2 = vs2 == expected2
    print(f"\nCase 2: n = (p² + 1)/2 = {n2}")
    print(f"  Value set: {sorted(vs2)}")
    print(f"  Expected:  {sorted(expected2)}")
    print(f"  Match: {'✓' if match2 else '✗'}")
    
    # Case 3: n = (p² + 2p - 1)/2, expected value set {1, p-1}
    n3 = (p**2 + 2*p - 1) // 2
    vs3 = compute_value_set(n3, p)
    expected3 = {1, p - 1}
    match3 = vs3 == expected3
    print(f"\nCase 3: n = (p² + 2p - 1)/2 = {n3}")
    print(f"  Value set: {sorted(vs3)}")
    print(f"  Expected:  {sorted(expected3)}")
    print(f"  Match: {'✓' if match3 else '✗'}")
    
    # Summary
    all_match = match1 and match2 and match3
    print(f"\n{'─'*60}")
    print(f"All cases verified: {'✓ PASS' if all_match else '✗ FAIL'}")
    
    return all_match


def main():
    print("Verification of Dickson Polynomial Value Sets with Cardinality 2")
    print("="*60)
    
    # Test on small primes first
    test_primes = [5, 7, 11, 13, 17, 19, 23, 29, 31]
    
    all_passed = True
    for p in test_primes:
        if is_prime(p):
            passed = verify_for_prime(p)
            all_passed = all_passed and passed
    
    print(f"\n\n{'='*60}")
    print(f"FINAL RESULT: {'ALL TESTS PASSED ✓' if all_passed else 'SOME TESTS FAILED ✗'}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
