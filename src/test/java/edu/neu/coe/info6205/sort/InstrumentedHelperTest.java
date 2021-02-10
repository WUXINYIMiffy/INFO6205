package edu.neu.coe.info6205.sort;

import edu.neu.coe.info6205.sort.simple.MergeSortBasic;
import edu.neu.coe.info6205.util.*;
import org.junit.BeforeClass;
import org.junit.Ignore;
import org.junit.Test;

import static org.junit.Assert.*;

public class InstrumentedHelperTest {

    @Test
    public void testInstrumented() {
        assertTrue(new InstrumentedHelper<String>("test", config).instrumented());
    }

    @Test
    public void testLess() {
        final Helper<String> helper = new InstrumentedHelper<>("test", config);
        assertTrue(helper.less("a", "b"));
        final PrivateMethodTester privateMethodTester = new PrivateMethodTester(helper);
        assertEquals(1, privateMethodTester.invokePrivate("getCompares"));
        assertEquals(0, privateMethodTester.invokePrivate("getSwaps"));
    }

    @Test
    public void testCompare() {
        String[] xs = new String[]{"a", "b"};
        final Helper<String> helper = new InstrumentedHelper<>("test", config);
        assertEquals(-1, helper.compare(xs, 0, 1));
        assertEquals(0, helper.compare(xs, 0, 0));
        assertEquals(1, helper.compare(xs, 1, 0));
        final PrivateMethodTester privateMethodTester = new PrivateMethodTester(helper);
        assertEquals(3, privateMethodTester.invokePrivate("getCompares"));
        assertEquals(0, privateMethodTester.invokePrivate("getSwaps"));
    }

    @Test
    public void testSwap1() {
        String[] xs = new String[]{"b", "a"};
        final Helper<String> helper = new InstrumentedHelper<>("test", config);
        final PrivateMethodTester privateMethodTester = new PrivateMethodTester(helper);
        assertEquals(1, helper.inversions(xs));
        assertEquals(0, privateMethodTester.invokePrivate("getFixes"));
        helper.swap(xs, 0, 1);
        assertArrayEquals(new String[]{"a", "b"}, xs);
        assertEquals(0, helper.inversions(xs));
        assertEquals(1, privateMethodTester.invokePrivate("getFixes"));
        helper.swap(xs, 0, 1);
        assertEquals(1, helper.inversions(xs));
        assertArrayEquals(new String[]{"b", "a"}, xs);
        // NOTE that we do not check fixes here because we did a non-fixing swap which will have generated an incorrect total.
        assertEquals(0, privateMethodTester.invokePrivate("getCompares"));
        assertEquals(2, privateMethodTester.invokePrivate("getSwaps"));
    }

    @Test
    public void testSwap2() {
        String[] xs = new String[]{"c", "b", "a"};
        final Helper<String> helper = new InstrumentedHelper<>("test", config);
        final PrivateMethodTester privateMethodTester = new PrivateMethodTester(helper);
        assertEquals(3, helper.inversions(xs));
        assertEquals(0, privateMethodTester.invokePrivate("getFixes"));
        helper.swap(xs, 0, 2);
        assertArrayEquals(new String[]{"a", "b", "c"}, xs);
        assertEquals(0, helper.inversions(xs));
        assertEquals(3, privateMethodTester.invokePrivate("getFixes"));
        helper.swap(xs, 0, 1);
        assertArrayEquals(new String[]{"b", "a", "c"}, xs);
        // NOTE that we do not check fixes here because we did a non-fixing swap which will have generated an incorrect total.
        assertEquals(0, privateMethodTester.invokePrivate("getCompares"));
        assertEquals(2, privateMethodTester.invokePrivate("getSwaps"));
    }

    @Test
    public void testSwap3() {
        String[] xs = new String[]{"c", "b", "d", "a"};
        final Helper<String> helper = new InstrumentedHelper<>("test", config);
        final PrivateMethodTester privateMethodTester = new PrivateMethodTester(helper);
        assertEquals(4, helper.inversions(xs));
        assertEquals(0, privateMethodTester.invokePrivate("getFixes"));
        helper.swap(xs, 0, 3);
        assertArrayEquals(new String[]{"a", "b", "d", "c"}, xs);
        assertEquals(1, helper.inversions(xs));
        assertEquals(3, privateMethodTester.invokePrivate("getFixes"));
        helper.swap(xs, 2, 3);
        assertArrayEquals(new String[]{"a", "b", "c", "d"}, xs);
        assertEquals(0, helper.inversions(xs));
        assertEquals(4, privateMethodTester.invokePrivate("getFixes"));
        assertEquals(0, privateMethodTester.invokePrivate("getCompares"));
        assertEquals(2, privateMethodTester.invokePrivate("getSwaps"));
    }

    @Test
    public void testSwap4() {
        String[] xs = new String[]{"c", "e", "b", "d", "a"};
        final Helper<String> helper = new InstrumentedHelper<>("test", config);
        final PrivateMethodTester privateMethodTester = new PrivateMethodTester(helper);
        assertEquals(7, helper.inversions(xs));
        assertEquals(0, privateMethodTester.invokePrivate("getFixes"));
        helper.swap(xs, 0, 4);
        assertArrayEquals(new String[]{"a", "e", "b", "d", "c"}, xs);
        assertEquals(4, helper.inversions(xs));
        assertEquals(3, privateMethodTester.invokePrivate("getFixes"));
        helper.swap(xs, 1, 4);
        assertArrayEquals(new String[]{"a", "c", "b", "d", "e"}, xs);
        assertEquals(1, helper.inversions(xs));
        assertEquals(6, privateMethodTester.invokePrivate("getFixes"));
        helper.swap(xs, 1, 2);
        assertArrayEquals(new String[]{"a", "b", "c", "d", "e"}, xs);
        assertEquals(0, helper.inversions(xs));
        assertEquals(7, privateMethodTester.invokePrivate("getFixes"));
        assertEquals(0, privateMethodTester.invokePrivate("getCompares"));
        assertEquals(3, privateMethodTester.invokePrivate("getSwaps"));
    }

    @Test
    public void testSwap5() {
        String[] xs = new String[]{"f", "e", "d", "c", "b", "a"};
        int n = xs.length;
        final Helper<String> helper = new InstrumentedHelper<>("test", config);
        final PrivateMethodTester privateMethodTester = new PrivateMethodTester(helper);
        int inversions = n * (n - 1) / 2;
        assertEquals(inversions, helper.inversions(xs));
        assertEquals(0, privateMethodTester.invokePrivate("getFixes"));
        helper.swap(xs, 0, n - 1);
        assertArrayEquals(new String[]{"a", "e", "d", "c", "b", "f"}, xs);
        int fixes = 2 * n - 3;
        assertEquals(fixes, privateMethodTester.invokePrivate("getFixes"));
        assertEquals(inversions - fixes, helper.inversions(xs));
        assertEquals(1, privateMethodTester.invokePrivate("getSwaps"));
    }

    @Test
    public void testSwap6() {
        String[] xs = new String[]{"g", "f", "e", "d", "c", "b", "a"};
        int n = xs.length;
        final Helper<String> helper = new InstrumentedHelper<>("test", config);
        final PrivateMethodTester privateMethodTester = new PrivateMethodTester(helper);
        int inversions = n * (n - 1) / 2;
        assertEquals(inversions, helper.inversions(xs));
        assertEquals(0, privateMethodTester.invokePrivate("getFixes"));
        helper.swap(xs, 0, n - 1);
        assertArrayEquals(new String[]{"a", "f", "e", "d", "c", "b", "g"}, xs);
        int fixes = 2 * n - 3;
        assertEquals(fixes, privateMethodTester.invokePrivate("getFixes"));
        assertEquals(inversions - fixes, helper.inversions(xs));
        assertEquals(1, privateMethodTester.invokePrivate("getSwaps"));
    }

    @Test
    public void testSorted() {
        String[] xs = new String[]{"a", "b"};
        final Helper<String> helper = new InstrumentedHelper<>("test", config);
        assertTrue(helper.sorted(xs));
        helper.swap(xs, 0, 1);
        assertFalse(helper.sorted(xs));
        final PrivateMethodTester privateMethodTester = new PrivateMethodTester(helper);
        assertEquals(0, privateMethodTester.invokePrivate("getCompares"));
        assertEquals(1, privateMethodTester.invokePrivate("getSwaps"));
    }

    @Test
    public void testInversions() {
        String[] xs = new String[]{"a", "b"};
        final Helper<String> helper = new InstrumentedHelper<>("test", config);
        assertEquals(0, helper.inversions(xs));
        helper.swap(xs, 0, 1);
        assertEquals(1, helper.inversions(xs));
    }

    @Test
    public void testPostProcess1() {
        String[] xs = new String[]{"a", "b"};
        final Helper<String> helper = new InstrumentedHelper<>("test", config);
        helper.init(3);
        helper.postProcess(xs);
    }

    @Test(expected = BaseHelper.HelperException.class)
    public void testPostProcess2() {
        String[] xs = new String[]{"b", "a"};
        final Helper<String> helper = new InstrumentedHelper<>("test", config);
        helper.postProcess(xs);
    }

    @Test
    public void testRandom() {
        String[] words = new String[]{"Hello", "World"};
        final Helper<String> helper = new InstrumentedHelper<>("test", 3, 0L, config);
        final String[] strings = helper.random(String.class, r -> words[r.nextInt(2)]);
        assertArrayEquals(new String[]{"World", "World", "Hello"}, strings);
    }

    @Test
    public void testToString() {
        final Helper<String> helper = new InstrumentedHelper<>("test", 3, config);
        assertEquals("Instrumenting helper for test with 3 elements", helper.toString());
    }

    @Test
    public void testGetDescription() {
        final Helper<String> helper = new InstrumentedHelper<>("test", 3, config);
        assertEquals("test", helper.getDescription());
    }

    @Test(expected = RuntimeException.class)
    public void testGetSetN() {
        final Helper<String> helper = new InstrumentedHelper<>("test", 3, config);
        assertEquals(3, helper.getN());
        helper.init(4);
        assertEquals(4, helper.getN());
    }

    @Test
    public void testGetSetNBis() {
        final Helper<String> helper = new InstrumentedHelper<>("test", config);
        assertEquals(0, helper.getN());
        helper.init(4);
        assertEquals(4, helper.getN());
    }

    @Test
    public void testClose() {
        final Helper<String> helper = new InstrumentedHelper<>("test", config);
        helper.close();
    }

    @Test
    public void testSwapStable() {
        String[] xs = new String[]{"a", "b"};
        final Helper<String> helper = new InstrumentedHelper<>("test", config);
        helper.swapStable(xs, 1);
        assertArrayEquals(new String[]{"b", "a"}, xs);
        helper.swapStable(xs, 1);
        assertArrayEquals(new String[]{"a", "b"}, xs);
        final PrivateMethodTester privateMethodTester = new PrivateMethodTester(helper);
        assertEquals(0, privateMethodTester.invokePrivate("getCompares"));
        assertEquals(2, privateMethodTester.invokePrivate("getSwaps"));
    }

    @Test
    public void testFixInversion1() {
        String[] xs = new String[]{"a", "b"};
        final Helper<String> helper = new InstrumentedHelper<>("test", config);
        final PrivateMethodTester privateMethodTester = new PrivateMethodTester(helper);
        helper.fixInversion(xs, 1);
        assertEquals(1, privateMethodTester.invokePrivate("getCompares"));
        assertEquals(0, privateMethodTester.invokePrivate("getSwaps"));
        assertArrayEquals(new String[]{"a", "b"}, xs);
        helper.swapStable(xs, 1);
        assertArrayEquals(new String[]{"b", "a"}, xs);
        helper.fixInversion(xs, 1);
        assertArrayEquals(new String[]{"a", "b"}, xs);
        assertEquals(2, privateMethodTester.invokePrivate("getCompares"));
        assertEquals(2, privateMethodTester.invokePrivate("getSwaps"));
    }

    @Test
    public void testFixInversion2() {
        String[] xs = new String[]{"a", "b"};
        final Helper<String> helper = new InstrumentedHelper<>("test", config);
        final PrivateMethodTester privateMethodTester = new PrivateMethodTester(helper);
        helper.fixInversion(xs, 0, 1);
        assertEquals(1, privateMethodTester.invokePrivate("getCompares"));
        assertEquals(0, privateMethodTester.invokePrivate("getSwaps"));
        assertArrayEquals(new String[]{"a", "b"}, xs);
        helper.swap(xs, 0, 1);
        assertArrayEquals(new String[]{"b", "a"}, xs);
        helper.fixInversion(xs, 0, 1);
        assertArrayEquals(new String[]{"a", "b"}, xs);
        assertEquals(2, privateMethodTester.invokePrivate("getCompares"));
        assertEquals(2, privateMethodTester.invokePrivate("getSwaps"));
    }

    @Test
    public void testMergeSort() {
        int N = 8;
        final Helper<Integer> helper = new InstrumentedHelper<>("test", config);
        final PrivateMethodTester privateMethodTester = new PrivateMethodTester(helper);
        Sort<Integer> s = new MergeSortBasic<>(helper);
        s.init(N);
        final Integer[] xs = helper.random(Integer.class, r -> r.nextInt(1000));
        s.sort(xs);
        final int compares = (Integer) privateMethodTester.invokePrivate("getCompares");
        assertTrue(compares <= 20 && compares >= 11);
    }

    @Ignore // TODO fix this test
    public void testMergeSortMany() {
        int N = 8;
        int m = 10;
        final Helper<Integer> helper = new InstrumentedHelper<>("test", config);
        final PrivateMethodTester privateMethodTester = new PrivateMethodTester(helper);
        Sort<Integer> s = new MergeSortBasic<>(helper);
        s.init(N);
        for (int i = 0; i < m; i++) {
            final Integer[] xs = helper.random(Integer.class, r -> r.nextInt(1000));
            Integer[] ys = s.sort(xs);
            helper.postProcess(ys);
        }
        final StatPack statPack = (StatPack) privateMethodTester.invokePrivate("getStatPack");
        final Statistics statistics = statPack.getStatistics(InstrumentedHelper.COMPARES);
        System.out.println(statistics);
        final int compares = statPack.getCount(InstrumentedHelper.COMPARES);
        System.out.println(statPack);
        assertTrue(12 <= compares && compares <= 17);
    }

    @BeforeClass
    public static void beforeClass() {
        config = ConfigTest.setupConfig("true", "0", "10", "1", "");
    }

    private static Config config;

    @Test
    public void swapInto() {
    }

    @Test
    public void testSwapConditional1() {
        String[] xs = new String[]{"c", "b", "a"};
        final Helper<String> helper = new InstrumentedHelper<>("test", config);
        assertFalse(helper.sorted(xs));
        helper.swapConditional(xs, 0, 2);
        assertTrue(helper.sorted(xs));
        final PrivateMethodTester privateMethodTester = new PrivateMethodTester(helper);
        assertEquals(1, privateMethodTester.invokePrivate("getCompares"));
        assertEquals(1, privateMethodTester.invokePrivate("getSwaps"));
    }

    @Test
    public void swapStableConditional() {
    }

    @Test
    public void copy() {
    }

    @Test
    public void incrementCopies() {
    }

    @Test
    public void incrementFixes() {
    }

    @Test
    public void testCompare1() {
    }

    @Test
    public void cutoff() {
    }

    @Test
    public void testToString1() {
    }

    @Test
    public void init() {
    }

    @Test
    public void preProcess() {
    }

    @Test
    public void postProcess() {
    }
}