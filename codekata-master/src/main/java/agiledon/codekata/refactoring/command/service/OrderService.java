package agiledon.codekata.refactoring.command.service;


import agiledon.codekata.refactoring.command.entity.Order;
import agiledon.codekata.refactoring.command.entity.ShoppingCart;
import agiledon.codekata.refactoring.command.infrastructure.DatabasePool;

import java.sql.*;

public class OrderService {
    private DatabasePool dbPool;

    public void addOrder(ShoppingCart cart, String userName, Order order) throws SQLException {
        Connection c = null;
        PreparedStatement ps = null;
        Statement s = null;
        ResultSet rs = null;
        boolean transactionState = false;
        try {
            s = c.createStatement();
            transactionState = c.getAutoCommit();
            int userKey = getUserKey(userName, c, ps, rs);
            c.setAutoCommit(false);
            addSingleOrder(order, c, ps, userKey);
            int orderKey = getOrderKey(s, rs);
            addLineItems(cart, c, orderKey);
            order.setOrderKeyFrom(orderKey);
            c.commit();
        } catch (SQLException sqlx) {
            s = c.createStatement();
            c.rollback();
            throw sqlx;
        } finally {
            try {
                c.setAutoCommit(transactionState);
                dbPool.release(c);
                if (s != null) s.close();
                if (ps != null) ps.close();
                if (rs != null) rs.close();
            } catch (SQLException ignored) {
            }
        }
    }

    private void addLineItems(ShoppingCart cart, Connection connection, int orderKey) {


    }

    private int getOrderKey(Statement statement, ResultSet rs) {
        return 0;
    }

    private void addSingleOrder(Order order, Connection connection, PreparedStatement ps, int userKey) {


    }

    private int getUserKey(String userName, Connection connection, PreparedStatement ps, ResultSet rs) {
        return 0;
    }
}
