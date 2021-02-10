package edu.neu.coe.info6205.greedy;

import org.junit.Test;

import java.util.Iterator;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertFalse;

public class ZeckendorfTest {
    /**
     * Test method for get
     */
    @Test
    public void testGet1() {
        Zeckendorf z = new Zeckendorf();
        Iterator<Long> fibs = z.get(10).iterator();
        assertEquals(new Long(8), fibs.next());
        assertEquals(new Long(2), fibs.next());
        assertFalse(fibs.hasNext());
    }

    /**
     * Test method for get
     */
    @Test
    public void testGet2() {
        Zeckendorf z = new Zeckendorf();
        Iterator<Long> fibs = z.get(100).iterator();
        assertEquals(new Long(89), fibs.next());
        assertEquals(new Long(8), fibs.next());
        assertEquals(new Long(3), fibs.next());
        assertFalse(fibs.hasNext());
    }

    /**
     * Test method for get
     */
    @Test
    public void testGet3() {
        Zeckendorf z = new Zeckendorf();
        Iterator<Long> fibs = z.get(1000).iterator();
        assertEquals(new Long(987), fibs.next());
        assertEquals(new Long(13), fibs.next());
        assertFalse(fibs.hasNext());
    }

    /**
     * Test method for get
     */
    @Test
    public void testGet4() {
        Zeckendorf z = new Zeckendorf();
        Iterator<Long> fibs = z.get(10000).iterator();
        assertEquals(new Long(6765), fibs.next());
        assertEquals(new Long(2584), fibs.next());
        assertEquals(new Long(610), fibs.next());
        assertEquals(new Long(34), fibs.next());
        assertEquals(new Long(5), fibs.next());
        assertEquals(new Long(2), fibs.next());
        assertFalse(fibs.hasNext());
    }

}
